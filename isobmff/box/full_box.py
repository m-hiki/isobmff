# -*- coding: utf-8 -*-
import re
from .box import Box


class FullBox(Box):
    box_type = None

    def __init__(self, size, version=None, flags=None):
        super().__init__(size)
        self.version = version
        self.flags = flags

    def __repr__(self):
        srep = super().__repr__()
        rep = ' v' + str(self.version) + '\n'
        return re.sub('\n', rep, srep, flags=re.MULTILINE)

    def get_box_size(self):
        """get box size excluding header"""
        return self.size - 12
