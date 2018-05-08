

class FieldMeta(type):
    def __new__(cls, name, bases, namespace):  # *args, **kwargs
        return type.__new__(cls, name, bases, namespace)


class Field(metaclass=FieldMeta):
    def __init__(self, size=None):
        self.size = size
        self.value = None

    def __get__(self, instance, owner=None):
        if instance:
            return self.value
        else:
            return self

    def __set__(self, instance, value):
        if instance:
            self.value = value
        else:
            pass

    def size(self): 
        return self.size if type(self.size) == 'int' else self.size.value

    def size_in_byte(self):
        return self.size() // 8

    def read(self, file):
        pass

    def write(self, file):
        pass
