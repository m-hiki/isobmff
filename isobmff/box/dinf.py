# -*- coding: utf-8 -*-
from .box import Box, Quantity, read_int, read_string
from .full_box import FullBox


class DataInformationBox(Box, box_type='dinf'):    
    is_mandatry = True
    quantity = Quantity.EXACTLY_ONE


class DataReferenceBox(FullBox, box_type='dref'):    
    is_mandatry = True
    quantity = Quantity.EXACTLY_ONE

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.data_entry = []

    def read(self, file):
        entry_count = read_int(file, 4)
        for _ in range(entry_count):
            box = Box()
            box.read(file)
            if not box:
                break
            self.data_entry.append(box)


class DataEntryUrlBox(FullBox, box_type='url '):    
    is_mandatry = True

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.location = None

    def read(self, file):
        self.location = read_string(file)


class DataEntryUrnBox(FullBox, box_type='urn '):    
    is_mandatry = True

    def __init__(self, size, version, flags):
        super().__init__(size=size, version=version, flags=flags)
        self.name = None
        self.location = None

    def read(self, file):
        self.name = read_string(file)
        self.location = read_string(file)
