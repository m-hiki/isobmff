from ..box import Box, Quantity, read_box, read_int, read_string
from ..full_box import FullBox


class ItemInformationBox(FullBox, boxtype='iinf'):
    is_mandatory = False

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.item_infos = []

    def read(self, file):
        count_size = 2 if self.version == 0 else 4
        entry_count = read_int(file, count_size)

        for _ in range(entry_count):
            box = read_box(file)
            if not box:
                break
            if box.box_type == 'infe':
                self.item_infos.append(box)
