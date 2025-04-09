def opcode_lda_immediate(cpu):
    value = cpu.fetch_byte()
    
    if value == 0:
        cpu.set_flag("ZERO", True)

    if value & 0x80: # if the leftmost bit is 1, it is negative (see two's complement)
        cpu.set_flag("NEGATIVE", True)

    cpu.a = value

OPCODE_TABLE = {
    0xA9: opcode_lda_immediate  # LDA immediate
}
