class RAM:
    def __init__(self, size: int = 65536):
        self.memory = bytearray(size)
        self.size = size

    def _check_bounds(self, address: int):
        if address < 0 or address >= self.size:
            raise ValueError("Address out of range")

    def read(self, address: int):
        self._check_bounds(address)
        return self.memory[address]
    
    def write(self, address: int, value: int):
        self._check_bounds(address)
        self.memory[address] = value
