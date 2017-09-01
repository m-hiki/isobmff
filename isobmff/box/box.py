# -*- coding: utf-8 -*-
from collections import OrderedDict
from enum import Enum
from .field import Field, Int, String
from io import BytesIO
import re


def gen_property(name, klass):
    storage_name = '_' + name
    
    @property
    def prop(self):
        print(self)
        return getattr(self, storage_name).value
    
    @prop.setter
    def prop(self, value):
        getattr(self, storage_name).value = value

    return prop


class BoxMeta(type):
    box_list = {}
    
    @classmethod
    def __prepare__(mcs, name, bases, *, box_type, extended_type=None):
        return OrderedDict()

    def __new__(mcs, clsname, bases, clsdict, *, box_type, extended_type=None):
        #clsdict['box_type'] = box_type        
        cls = type.__new__(mcs, clsname, bases, dict(clsdict))
        if box_type:
            mcs.box_list[box_type] = cls
        
        fields = ((k, v) for k, v in clsdict.items() if isinstance(v, Field))
        cls.fields = OrderedDict(fields)

        # Field object is renamed and replaced to property
        for name, field in cls.fields.items():
            setattr(cls, '_' + name, field)
            setattr(cls, name, gen_property(name, field))
        return cls

    def __init__(self, clsname, bases, clsdict, *, box_type, extended_type=None):
        super().__init__(clsname, bases, clsdict)


class Box(metaclass=BoxMeta, box_type=None):
    size = Int(32)
    typ = String(32)

    def get_box_size(self):
        """get box size excluding header"""
        return self.size - 8

    def read_field(self, file):
        for name, field in self.fields.items():
            field.read(file)
            #print(name + ' ' + str(field))
        
    def read(self, file):
        self.read_field(file)
        box_size = self.size - (self._size.size + self._typ.size)
        buff = BytesIO(file.read(box_size))
        #print(self.typ + '(' + str(self.size) + ')')
        for cls in get_class_tree(Box, BoxMeta.box_list[self.typ]):
            self.__class__ = cls
            self.read_field(buff)

    def write(self, file):
        """write box to file"""
        pass


class Quantity(Enum):
    ZERO_OR_ONE = 0
    EXACTLY_ONE = 1
    ONE_OR_MORE = 2
    ANY_NUMBER = 3


class BoxContainer(Field):
    def read(self, file):
        self.value = []
        read_size = self.size

        while read_size > 0:
            box = Box()
            box.read(file)
            #TODO: Quantityでそのままsetattrか配列にappendか分ける
            if not box.size:
                break
            self.value.append(box)
            read_size -= box.size

def indent(rep):
    return re.sub(r'^', '  ', rep, flags=re.M)


def get_class_tree(cls, target):
    tree = []
    while target != cls:
        tree.insert(0, target)
        target = target.__base__
    return tree

