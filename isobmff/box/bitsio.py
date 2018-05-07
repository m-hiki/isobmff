from io import BytesIO


class BitsIO(BytesIO):
    """BitsIO
       msb first
    """

    def __init__(self, file):
        super().__init__(file)
        self.value = 0
        self.left = 8

    def read_bytes(self, size=1):
        return int.from_bytes(self.read(size), byteorder='big')

    def read_bits(self, size=1):
        if self.left == 8:
            self.value = self.read_bytes(1)
        left = self.left - size
        mask = (1 << size) - 1
        res = (self.value >> left) & mask
        self.left = 8 if left == 0 else left
        return res
