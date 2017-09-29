from .box.box import Box, indent
import os


class MediaFile(object):

    
    def __init__(self):
        self.ftyp = None
        self.mdats = []
        self.meta = None
        self.moov = None

    def __repr__(self):
        rep = self.ftyp.__repr__() + '\n'
        rep += self.meta.__repr__() + '\n'
        rep += self.moov.__repr__() + '\n'
        for mdat in self.mdats:
            rep += mdat.__repr__() + '\n'
        return 'ISOBaseMediaFile\n' + indent(rep)

    def read(self, file_name):
        read_size = os.path.getsize(file_name)
        with open(file_name, 'rb') as file:
            while read_size:
                box = Box()
                box.read(file)
                if not box:
                    break
                #if box.box_type == 'mdat':
                #    self.mdats.append(box)
                #else:
                #setattr(self, box.box_type, box)
                #    pass
                read_size -= box.size
