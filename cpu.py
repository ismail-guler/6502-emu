from instructions import OPCODE_TABLE
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
        opcode = self.fetch_byte()
        if opcode in OPCODE_TABLE:
            OPCODE_TABLE[opcode](self)
        else:
            raise Exception(f"Opcode {opcode:#04x} not found")

    def fetch_byte(self): # fetches next byte at PC
        value = self.ram.read(self.pc)
        self.pc += 1
        return value

    def fetch_word(self):
        low = self.fetch_byte() # low byte
        high = self.fetch_byte() # high byte
        return high << 8 | low # shift high 8 bits, then add 'low' to lower bits with 'or' operation.
