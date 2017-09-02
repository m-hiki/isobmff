# -*- coding: utf-8 -*-
from collections import OrderedDict
from .field import Field


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
