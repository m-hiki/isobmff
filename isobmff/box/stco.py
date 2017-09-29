from .box import Box, Quantity, read_box, read_int, read_string
from .full_box import FullBox

class ChunkOffsetBox(FullBox, box_type='stco'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.entries = []

    def read(self, file):
        entry_count = read_int(file, 4)

        for _ in range(entry_count):
            entry = {}
            entry['chunk_offset'] = read_int(file, 4)
            self.entries.append(entry)