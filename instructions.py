def opcode_lda_immediate(cpu):
    value = cpu.fetch_byte()
    cpu.a = value

OPCODE_TABLE = {
    0xA9: opcode_lda_immediate  # LDA immediate
}
