from .box import Quantity
from .full_box import ContainerFullbox

class MetaBox(ContainerFullbox, boxtype='meta'):    
    is_mandatory = False
    quntity = Quantity.ZERO_OR_ONE
