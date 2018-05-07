from ..box import Box, Quantity, read_box, read_int, read_string
from ..iso14496_12.stbl import VisualSampleEntry


class HEVCSampleEntry(VisualSampleEntry, box_type='hvc1'):
    is_mandatry = True
    quantity = Quantity.ONE_OR_MORE

    def __init__(self, size):
        super().__init__(size=size)
        self.config = None

    def read(self, file):
        super().read(file)
        self.config = read_box(file)
