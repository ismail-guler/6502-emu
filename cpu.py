class CPU:
    def __init__(self, ram):
        self.ram = ram
        self.a, self.x, self.y = 0 # a, x, y registers
        self.pc = 0x0000 # program counter
        self.sp = 0xFD # stack pointer, 6502 default is 0xFD
        self.status = 0x00 # flags

    def reset(self):
        self.a = self.x = self.y = 0
        self.pc = 0x0000
        self.sp = 0xFD
        self.status = 0x00
 

    def step(self):
        pass