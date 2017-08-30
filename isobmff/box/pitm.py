# -*- coding: utf-8 -*-
from .box import Box, Quantity, read_box, read_int, read_string
from .full_box import FullBox

class PrimaryItemBox(FullBox, box_type='pitm'):    
    is_mandatory = False

    def read(self, file):
        self.item_id = read_int(file, 2)
