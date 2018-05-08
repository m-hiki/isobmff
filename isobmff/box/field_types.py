from copy import deepcopy
from .field import Field


class Bit(Field):
    def read(self, file):
        self.value = file.read_bits(self.size)


class Container(Field):
    """Container
       read object to box end and save to list
    """

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

        # for item in self.value:
        #    print(item.value)


class DataLocation(Field):
    def read(self, file):
        self.value = file.tell()


class Int(Field):
    def read(self, file):
        size = self.size_in_byte()
        self.value = int.from_bytes(file.read(size), byteorder='big')


class String(Field):
    def read(self, file):
        # TODO: convert utf8
        if self.size:
            res = file.read(self.size_in_byte()).decode()
        else:
            res = ''.join(iter(lambda: file.read(1).decode('ascii'), '\x00'))
        self.value = res


class List(Field):
    def __init__(self, size, obj):
        super().__init__(size)
        self.obj = obj

    def read(self, file):
        self.value = []
        for _ in range(self.size):
            item = deepcopy(self.obj)
            item.read(file)
            self.value.append(item)


class Entry(Field):
    def __init__(self, count, **args):
        super().__init__(None)
        self.count = count
        self.objs = dict(args)

    def read(self, file):
        self.value = []
        self.count.read(file)
        print('-------')
        for _ in range(self.count.value):
            items = {}
            for name, obj in self.objs.items():
                item = deepcopy(obj)
                item.read(file)
                items[name] = item
            self.value.append(item)
