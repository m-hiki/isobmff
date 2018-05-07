from .box import Box, Quantity, read_box, read_int, read_string
from .full_box import FullBox


class ItemPropertiesBox(Box, box_type='iprp'):
    is_mandatry = False
    quantity = Quantity.ZERO_OR_ONE


class ItemPropertyContainer(Box, box_type='ipco'):
    is_mandatry = True
    quantity = Quantity.EXACTLY_ONE


class ImageSpatialExtents(FullBox, box_type='ispe'):
    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.width = None
        self.height = None

    def read(self, file):
        self.width = read_int(file, 4)
        self.height = read_int(file, 4)


class PixelAspectRatio(Box, box_type='pasp'):
    def read(self, file):
        print(file.read(self.get_box_size()))


class ColorInformation(Box, box_type='colr'):
    def read(self, file):
        print(file.read(self.get_box_size()))


class PixelInformation(Box, box_type='pixi'):
    def read(self, file):
        print(file.read(self.get_box_size()))


class RelativeInformation(Box, box_type='rloc'):
    def read(self, file):
        print(file.read(self.get_box_size()))
