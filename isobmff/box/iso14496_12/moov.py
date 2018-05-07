from ..box import Box, Quantity


class MovieBox(Box, box_type='moov'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE
