# -*- coding: utf-8 -*-
from .field import Bit, Entry, Int, List, String
from .full_box import FullBox

class ItemLocationBox(FullBox, boxtype='iloc'):    
    is_mandatory = False
    offset_size = Bit(4)
    length_size = Bit(4)
    base_offset_size = Bit(4)
    reserved = Bit(4)
    item_count = Int(16)
    #item = List()
    class Item(Entry):
        item_id = Int(16)
        data_reference_index = Int(16)
        #base_offset = Int(base_offset_size)
        extent_count = Int(16)
        class Extent(Entry):
            extent_offset = Int(offset_size)
            extent_lengh = Int(length_size)
        extents = Extent(extent_count)
    items = Item(item_count)
    #items = List()
    
"""
        item_count = read_int(file, 2)

        for _ in range(item_count):
            item = {}
            item['item_id'] = read_int(file, 2)
            item['data_reference_index'] = read_int(file, 2)
            item['base_offset'] = read_int(file, self.base_offset_size)
            extent_count = read_int(file, 2)
            item['extents'] = []
            for _ in range(extent_count):
                extent = {}
                extent['extent_offset'] = read_int(file, self.offset_size)
                extent['extent_length'] = read_int(file, self.length_size)
                item['extents'].append(extent)
            self.items.append(item)

"""