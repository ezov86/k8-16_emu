from itypes import u8, u16


class Flags:
    def __init__(self):
        self.fC = 0
        self.fN = 0
        self.fZ = 0
        self.fI = 0

    def get_u8(self) -> u8:
        return u8(self.fC | self.fN << 1 | self.fZ << 2 | self.fI << 3)


class Cpu:
    def __init__(self):
        self.FLAGS = Flags()

        self.rA = u8(0)
        self.rB = u8(0)
        self.rX = u8(0)
        self.rY = u8(0)

        self.rIPH = u8(0)
        self.rIPL = u8(0)
        self.rSPH = u8(0)
        self.rSPL = u8(0)
        self.rMD = u8(0)

        self.rTMP = u8(0)

    def next_microinst(self):
        pass


