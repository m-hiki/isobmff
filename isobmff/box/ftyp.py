# -*- coding: utf-8 -*-
from .box import Box, Quantity
from .field import Int, String, ListToBoxEnd


class FileTypeBox(Box, box_type='ftyp'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE
    majar_brand = String(32)
    minor_version = String(32)
    compatible_brands = ListToBoxEnd(String(32))
