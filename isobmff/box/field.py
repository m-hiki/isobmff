# -*- coding: utf-8 -*-
from copy import deepcopy


class Field(object):
    def __init__(self, size=None):
        if size:
            self.size = int(size / 8) # bit to byte
        self.value = None

    def read(self, file):
        pass

    def write(self, file):
        pass


class Int(Field):    
    def read(self, file):
        data = file.read(self.size)
        self.value = int.from_bytes(data, byteorder='big', signed=False)


class String(Field):
    def read(self, file):
        #TODO: convert utf8
        if self.size:
            res = file.read(self.size).decode()
        else:
            res = ''.join(iter(lambda: file.read(1).decode('ascii'), '\x00'))
        self.value = res


class DataLocation(Field):
    def read(self, file):
        self.value = file.tell()


class ListToBoxEnd(Field):
    def __init__(self, obj):
        super().__init__(None)
        self.obj = obj

    def read(self, file):
        self.value = []
        size = len(file.getbuffer())
        while size > 0:
            item = deepcopy(self.obj)
            item.read(file)
            self.value.append(item)
            size -= self.obj.size

        #for item in self.value:
        #    print(item.value)
