# -*- coding: utf-8 -*-
from .box import Quantity
from .full_box import FullBox

class MetaBox(FullBox, box_type='meta'):    
    is_mandatory = False
    quntity = Quantity.ZERO_OR_ONE
