# -*- coding: utf-8 -*-
from .field import Bit, Entry, Int, List, String
from .full_box import FullBox


class ItemLocationBox(FullBox, boxtype='iloc'):    
    is_mandatory = False
    offset_size = Bit(4)
    length_size = Bit(4)
    base_offset_size = Bit(4)
    reserved = Bit(4)
    items = Entry(count=Int(16),
                  item_id = Int(16),
                  data_reference_index = Int(16),
                  base_offset = Int(base_offset_size.value),
                  extents = Entry(count=Int(16),
                                  extent_offset = Int(offset_size.value),
                                  extent_lengh = Int(length_size.value)))
