from enum import Enum
from .base import BoxIO
from .field import Int, String, Container
from .bitsio import BitsIO
import re


class Box(BoxIO):
    size = Int(32)
    typ = String(32)

    def get_box_size(self):
        """get box size excluding header"""
        return self.size - (Box.size.size + Box.typ.size)
        
    def read(self, file):
        super().read(file)
        buff = BitsIO(file.read(self.get_box_size()))
        print(self.typ + '(' + str(self.size) + ')')

        for cls in get_class_tree(Box, Box.box_list[self.typ]):
            self.__class__ = cls
            super().read(buff)

    def write(self, file):
        """write box to file"""


class ContainerBox(Box):
    container = Container(Box())
    """
    def read(self, file):
        self.value = []
        read_size = self.size

        while read_size > 0:
            box = Box()
            box.read(file)
            #TODO: Quantityでそのままsetattrか配列にappendか分ける
            if not box.size:
                break
            self.value.append(box)
            read_size -= box.size
    """

class Quantity(Enum):
    ZERO_OR_ONE = 0
    EXACTLY_ONE = 1
    ONE_OR_MORE = 2
    ANY_NUMBER = 3

def indent(rep):
    return re.sub(r'^', '  ', rep, flags=re.M)

def get_class_tree(cls, target):
    tree = []
    while target != cls:
        tree.insert(0, target)
        target = target.__base__
    return tree