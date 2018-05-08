from collections import OrderedDict
from .field import Field


class BoxMeta(type):
    box_list = {}

    @classmethod
    def __prepare__(cls, name, bases, *, boxtype=None):
        return OrderedDict()

    def __new__(cls, name, bases, namespace, *, boxtype=None):
        clsobj = type.__new__(cls, name, bases, dict(namespace))
        fields = ((k, v) for k, v in namespace.items() if isinstance(v, Field))
        clsobj.fields = OrderedDict(fields)
        if boxtype:
            cls.box_list[boxtype] = clsobj
        return clsobj

    def __init__(self, name, bases, namespace, *, boxtype=None):
        super().__init__(name, bases, namespace)


class BoxIO(metaclass=BoxMeta):
    def read(self, file):
        for name, field in self.fields.items():
            field.read(file)
            print(name)
