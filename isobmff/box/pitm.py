from .box import Quantity
from .field import Int
from .full_box import FullBox

class PrimaryItemBox(FullBox, boxtype='pitm'):    
    is_mandatory = False

    item_id = Int(16)
