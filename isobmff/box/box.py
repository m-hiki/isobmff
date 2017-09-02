# -*- coding: utf-8 -*-
from enum import Enum
from .box_meta import BoxMeta
from .field import Field, Int, String
from io import BytesIO
import re


class BaseBox(metaclass=BoxMeta, box_type=None):
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


def get_class_tree(cls, target):
    tree = []
    while target != cls:
        tree.insert(0, target)
        target = target.__base__
    return tree


class Box(BaseBox, box_type=None):
    size = Int(32)
    typ = String(32)


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
