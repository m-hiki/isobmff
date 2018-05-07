from .box import Box, Quantity, read_box, read_int, read_string
from ..full_box import FullBox


class MovieHeaderBox(FullBox, box_type='mvhd'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE

    #read_size = 8 if self.version == 1 else 4
    creation_time = Int(32)  # TODO: or 64
    modification_time = Int(32)  # TODO: or 64
    timescale = Int(32)
    duration = Int(32)  # TODO: or 64
    rate = Int(32)
    volume = Int(16)
    reserved1 = int(16)
    reserved2 = List(2, Int(32))
    matrix = List(9, Int(32))
    pre_defined = List(6, Int(32))
    next_track_id = Int(32)
