from typing import Tuple
import logging


class DeviceInterface:
    def write(self, offset: int, data: int):
        pass

    def read(self, offset: int) -> int:
        pass

    def get_code(self) -> int:
        pass


class AddressSpace:
    def __init__(self, start: int, end: int):
        assert start <= end <= 2 ** 16

        self.start = start
        self.end = end

    def is_in(self, address: int) -> bool:
        return self.start <= address <= self.end


class Bus:
    def __init__(self, memory_map: Tuple[AddressSpace, DeviceInterface]):
        self.map = memory_map

    def _send_io(self, address: int, data: int, do_read: bool) -> int:
        for space, device in self.map:
            if space.is_in(address):
                offset = address - address
                if do_read:
                    return device.read(offset)
                else:
                    device.write(offset, data)
                    return 0

        logging.warning('[BUS] No devices mapped to %04X (data %02X)' % (address, data))
        return 0xEB  # Magic number that means no devices mapped (for debugging purpose)

    def read(self, address: int) -> int:
        return self._send_io(address, 0, True)

    def write(self, address: int, data: int):
        self._send_io(address, data, False)
