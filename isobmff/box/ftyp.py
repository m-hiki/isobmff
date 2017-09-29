from .box import Box, Quantity
from .field import Int, String, Container


class FileTypeBox(Box, boxtype='ftyp'):
    is_mandatory = True
    quantity = Quantity.EXACTLY_ONE
    majar_brand = String(32)
    minor_version = String(32)
    compatible_brands = Container(String(32))
