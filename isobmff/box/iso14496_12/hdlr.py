from ..box import Quantity
from ..field import Int, List, String
from ..full_box import FullBox


class HandlerReferenceBox(FullBox, boxtype='hdlr'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE

    pre_defined = Int(32)
    handler_type = String(32)
    reserved = List(3, Int(32))
    name = String(32)
