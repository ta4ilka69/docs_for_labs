org 0x0000
OUTP:
    IN 0x15
    AND #0x40
    BEQ OUTP
    LD #0
    OUT 0x14
    LD #0x1B
    OUT 0x14
    LD #0x2B
    OUT 0x14
    LD #0x3B
    OUT 0x14
    LD #0x4B
    OUT 0x14
    LD #0x5B
    OUT 0x14
    LD #0x6B
    OUT 0x14
    LD #0x7B
    OUT 0x14
    HLT