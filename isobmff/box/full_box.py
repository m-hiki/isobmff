from .box import Box
from .field import Int, Container

class FullBox(Box, boxtype=None):
    version = Int(8)
    flags = Int(24)

    def get_box_size(self):
        """get box size excluding header"""
        header_size = FullBox.version.size + FullBox.flags.size
        return super().get_box_size - header_size


class ContainerFullbox(FullBox, boxtype=None):
    container = Container(Box())