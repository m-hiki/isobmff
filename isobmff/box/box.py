# -*- coding: utf-8 -*-
from collections import OrderedDict
from enum import Enum
import re
from .field import Field, Int, String


class BoxMeta(type):
    box_list = {}
    
    @classmethod
    def __prepare__(mcs, name, bases, *, box_type):
        return OrderedDict()

    def __new__(mcs, clsname, bases, clsdict, *, box_type):
        clsdict['box_type'] = box_type
        cls = type.__new__(mcs, clsname, bases, clsdict)        
        if box_type:
            mcs.box_list[box_type] = cls
        fields = ((k, v) for k, v in clsdict.items() if isinstance(v, Field))
        cls.fields = OrderedDict(fields)
        return cls

    def __init__(self, clsname, bases, clsdict, *, box_type):
        super().__init__(clsname, bases, clsdict)


class Box(metaclass=BoxMeta, box_type=None):
    size = Int(32)
    typ = String(32)

    @classmethod
    def get_class_tree(cls, target):
        tree = []
        while target != cls:
            tree.insert(0, target)
            target = target.__base__
        return tree

    def get_box_size(self):
        """get box size excluding header"""
        return self.size - 8

    def read_field(self, file):
        for name, field in self.fields.items():            
            field.read(file)
            print(name + ' ' + str(field.value))
        
    def read(self, file):
        self.read_field(file)
        tree = Box.get_class_tree(BoxMeta.box_list[self.typ.value])
        for cls in tree:
            self.__class__ = cls
            self.read_field(file)

    def write(self, file):
        """write box to file"""
        pass

class Container(object):
    def read(self, file):
        read_size = self.get_box_size()
        #print(file.read(read_size))
        while read_size > 0:
            box = read_box(file)
            if not box:
                break
            #TODO: Quantityでそのままsetattrか配列にappendか分ける
            setattr(self, box.box_type, box)
            read_size -= box.size

class Quantity(Enum):
    ZERO_OR_ONE = 0
    EXACTLY_ONE = 1
    ONE_OR_MORE = 2
    ANY_NUMBER = 3

def indent(rep):
    return re.sub(r'^', '  ', rep, flags=re.M)
