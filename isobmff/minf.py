# -*- coding: utf-8 -*-
from .box import Box
from .box import FullBox
from .box import indent
from .box import read_box
from .box import read_int


class MediaInformationBox(Box):
    """Media Information Box
    """
    box_type = 'minf'
    is_mandatory = True
    #Quantity: Exactly one

    def read(self, file):
        read_size = self.get_box_size()
        while read_size > 0:
            box = read_box(file)
            if not box:
                break
            setattr(self, box.box_type, box)
            read_size -= box.size


class VideoMediaHeaderBox(FullBox):
    """Video Media Header Box
    """
    box_type = 'vmhd'
    is_mandatory = True

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.graphicsmode = None
        self.opcolor = []

    def read(self, file):
        self.graphicsmode = read_int(file, 2)
        for _ in range(3):
            self.opcolor.append(read_int(file, 2))


class SoundMediaHeaderBox(FullBox):
    """Sound Media Header Box
    """
    box_type = 'smhd'
    is_mandatory = True

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.balance = None
        self.reserved = None

    def read(self, file):
        self.balance = read_int(file, 2)
        self.reserved = read_int(file, 2)


class HintMediaHeaderBox(FullBox):
    """Hint Media Header Box
    """
    box_type = 'hmhd'
    is_mandatory = True

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.max_pdu_size = None
        self.avg_pdu_size = None
        self.max_bit_rate = None
        self.avg_bit_rate = None
        self.reserved = None

    def read(self, file):
        self.max_pdu_size = read_int(file, 2)
        self.avg_pdu_size = read_int(file, 2)
        self.max_bit_rate = read_int(file, 4)
        self.avg_bit_rate = read_int(file, 4)
        self.reserved = read_int(file, 4)


class NullMediaHeaderBox(FullBox):
    """Null Media Header Box
    """
    box_type = 'nmhd'
    is_mandatory = True
