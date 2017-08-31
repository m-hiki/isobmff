# -*- coding: utf-8 -*-



class Field(object):
    def __init__(self, size):
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
