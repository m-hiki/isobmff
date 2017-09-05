
# -*- coding: utf-8 -*-
from functools import wraps

class Field:
    def __init__(self, size):
        self.size = size // 8
        self.value = None

    def read(self, file):
        pass
    
    def write(self, file):
        pass

class Int(Field):
    def read(self, file):
        self.value =  int.from_bytes(file.read(self.size), byteorder='big')

class String(Field):
    def read(self, file):
        if self.size:
            res = file.read(self.size).decode()
        else:
            res = ''.join(iter(lambda: file.read(1).decode('ascii'), '\x00'))
        self.value = res

def defbox(extend):
    def _defbox(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if extend:
                for gen in extend:
                    yield gen
            for gen in func(*args, **kwargs):
                yield gen
        return wrapper
    return _defbox

#@defbox(extend=None)
def box(boxtype=None):
    size = Int(32)
    typ = String(32)
    def gen():
        yield size
        yield typ
    return gen

#@defbox(extend=box())
def full_box():
    version = Int(8)
    flags = Int(24)
    def gen():
        yield version
        yield flags
    return gen

#@defbox(extend=box('ftyp'))
def ftyp():
    major_brand = String(32)
    minor_version = Int(32)
    compatible_brands = String(32)
    def gen():
        yield major_brand
        yield minor_version
        yield compatible_brands
    return gen

@defbox(extend=box('moov'))
def movie_box():
    pass

if __name__ == '__main__':
    with open('C001.heic', 'rb') as file:
        b = box()
        for field in b():
            field.read(file)
            print(field.value)
        
        for field in b():
            print(field.value)
    eval('ftyp')()