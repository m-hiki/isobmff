from .box import Box, Quantity, read_box, read_int, read_string
from .full_box import FullBox


class TrackBox(Box, box_type='trak'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE
