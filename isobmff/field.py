# -*- coding: utf-8 -*-



class Field(object):
    def __init__(self, name):
        self.name = name
        self.value = None

    def read(self, file):
        pass

    def write(self, file):
        pass


class IntField(Field):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    
    def read(self, file):
        data = file.read(self.size)
        self.value = int.from_bytes(data, byteorder='big', signed=False)


class StringField(Field):

    def read(self, file):
        #TODO: convert utf8
        if self.length:
            res = file.read(self.length).decode()
        else:
            res = ''.join(iter(lambda: file.read(1).decode('ascii'), '\x00'))
        self.value = res
