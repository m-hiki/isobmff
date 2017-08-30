# -*- coding: utf-8 -*-
import re
from enum import Enum


class BoxMeta(type):
    box_list = {}
    
    def __new__(mcs, clsname, bases, clsdict, *, box_type):
        clsdict['box_type'] = box_type
        cls = type.__new__(mcs, clsname, bases, clsdict)        
        if box_type:
            mcs.box_list[box_type] = cls
        return cls

    def __init__(self, clsname, bases, clsdict, *, box_type):
        super().__init__(clsname, bases, clsdict)


class Box(metaclass=BoxMeta, box_type=None):
    def __init__(self, size=None):
        self.size = size
        self.largesize = None

    def get_box_size(self):
        """get box size excluding header"""
        return self.size - 8

    def read(self, file):
        self.size = read_int(file, 4)
        self.box_type = read_string(file, 4)
        print(self.box_type + '(' + str(self.size) + ')')
        #print(BoxMeta.box_list)
        self.__class__ = BoxMeta.box_list[self.box_type]
        if self.__class__.__base__.__name__ == 'FullBox':
            self.version = read_int(file, 1)
            self.flags = read_int(file, 3)
        if self.get_box_size():
            self.read(file)

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

def read_int(file, length):
    return int.from_bytes(file.read(length), byteorder='big', signed=False)

def read_string(file, length=None):
    #TODO: convert utf8
    if length:
        res = file.read(length).decode()
    else:
        res = ''.join(iter(lambda: file.read(1).decode('ascii'), '\x00'))
    return res

def indent(rep):
    return re.sub(r'^', '  ', rep, flags=re.M)

def read_box(file):
    """
    size = read_int(file, 4)
    box_type = read_string(file, 4)
    print(box_type + '(' + str(size) + ')')
    #print(BoxMeta.box_list)
    box = BoxMeta.box_list[box_type]()
    if box.__base__.__name__ == 'FullBox':
        version = read_int(file, 1)
        flags = read_int(file, 3)
    if box.get_box_size():
        box.read(file)    
    """
    box = Box()
    box.read(file)

    return box
