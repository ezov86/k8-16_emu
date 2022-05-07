import logging
from bus import DeviceInterface


class Ram(DeviceInterface):
    def __init__(self, size: int):
        assert size < 2 ** 16

        self.size = size
        self.values = [0] * size

    def read(self, offset: int) -> int:
        return self.values[offset]

    def write(self, offset, data):
        if offset >= self.size:
            logging.warning('[device:RAM] address %04X is out of range (total size: %d bytes)' % (offset, self.size))
            return

        self.values[offset] = data

    def get_code(self) -> int:
        return 0x01  # RAM code.
