from instructions import OPCODE_TABLE

FLAG_TABLE = {
    "NEGATIVE"  : 0b10000000,  # 7
    "OVERFLOW"  : 0b01000000,  # 6
    "UNUSED"    : 0b00100000,  # 5 - always 1
    "BREAK"     : 0b00010000,  # 4
    "DECIMAL"   : 0b00001000,  # 3
    "INTERRUPT" : 0b00000100,  # 2
    "ZERO"      : 0b00000010,  # 1
    "CARRY"     : 0b00000001   # 0
}

class CPU:
    def __init__(self, ram):
        self.ram = ram
        self.a = self.x = self.y = 0 # a, x, y registers
        self.pc = 0x0000 # program counter
        self.sp = 0xFD # stack pointer, 6502 default is 0xFD
        self.status = 0x00 # flags

        self.clear_flags()

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

    def set_flag(self, flag_name: str, condition: bool):
        bit = FLAG_TABLE[flag_name]
        if condition:
            self.status |= bit  # set flag if condition is true
        else:
            self.status &= ~bit # remove only our flag, dont touch other flags. See this operation with examples for explanation
    
    def get_flag(self, flag_name: str):
        bit = FLAG_TABLE[flag_name]
        flag = bit & self.status # get only the bit of the flag 
        return (self.status & bit) != 0
    
    def clear_flags(self):
        for flag_name in FLAG_TABLE.keys():
            self.set_flag(flag_name, False)
        
        self.set_flag("UNUSED", True)