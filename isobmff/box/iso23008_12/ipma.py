from ..box import Box, Quantity, read_box, read_int, read_string
from ..full_box import FullBox


class ItemPropertyAssociation(FullBox, box_type='ipma'):
    is_mandatry = True
    quantity = Quantity.EXACTLY_ONE

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.items = []

    def read(self, file):
        entry_count = read_int(file, 4)
        id_size = 2 if self.version < 1 else 4
        for _ in range(entry_count):
            item = {}
            item['id'] = read_int(file, id_size)
            association_count = read_int(file, 1)
            item['associations'] = []
            for __ in range(association_count):
                association = {}
                if self.flags & 0b1:
                    byte = read_int(file, 2)
                    association['essential'] = (byte >> 15) & 0b1
                    association['property_index'] = byte & 0b111111111111111
                else:
                    byte = read_int(file, 1)
                    association['essential'] = (byte >> 7) & 0b1
                    association['property_index'] = byte & 0b1111111
                item['associations'].append(association)
            self.items.append(item)
