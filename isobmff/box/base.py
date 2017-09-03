# -*- coding: utf-8 -*-
from collections import OrderedDict


class OrderedFieldMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, *, boxtype, extended_type=None):
        return OrderedDict()

    def __new__(mcs, clsname, bases, clsdict):
        cls = type.__new__(mcs, clsname, bases, dict(clsdict))
        fields = ((k, v) for k, v in clsdict.items() if isinstance(v, Field))
        cls.fields = OrderedDict(fields)
        return cls


class BoxMeta(OrderedFieldMeta):
    box_list = {}

    @classmethod
    def __prepare__(mcs, name, bases, *, boxtype, extended_type=None):
        return OrderedDict()

    def __new__(mcs, clsname, bases, clsdict, *, boxtype, extended_type=None):
        #clsdict['box_type'] = box_type
        cls = super().__new__(mcs, clsname, bases, clsdict)
        if boxtype:
            mcs.box_list[boxtype] = cls
        return cls

    def __init__(self, clsname, bases, clsdict, *, boxtype, extended_type=None):
        super().__init__(clsname, bases, clsdict)


class Field(metaclass=OrderedFieldMeta):
    def __init__(self, size=None):
        if size:
            self.size = size // 8 # bit to byte
        self.value = None

    def __get__(self, obj, type=None):
        if obj:
            return self.value
        else:
            return self
    
    def __set__(self, obj, value):
        pass

    def read(self, file):
        pass

    def write(self, file):
        pass
