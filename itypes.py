from ctypes import c_uint8, c_uint16


class u8(c_uint8):
    def __add__(self, other):
        return u8(self.value + other.value)

    def __sub__(self, other):
        return u8(self.value - other.value)


class u16(c_uint16):
    def __add__(self, other):
        return u16(self.value + other.value)

    def __sub__(self, other):
        return u16(self.value - other.value)
