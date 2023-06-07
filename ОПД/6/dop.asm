ORG 0x000
V0: WORD $INT0, 0x180
V1: WORD $INT1, 0x180
V2: WORD $INT2, 0x180
V3: WORD $DEFAULT, 0x180
V4: WORD $DEFAULT, 0x180
V5: WORD $DEFAULT, 0x180
V6: WORD $DEFAULT, 0x180
V7: WORD $DEFAULT, 0x180
DEFAULT: IRET

T0: WORD 0x000B
T1: WORD 0x001B
T2: WORD 0x002B
T3: WORD 0x003B
T4: WORD 0x004B
T5: WORD 0x005B
T6: WORD 0x006B

TS: WORD 0x0000

TIME: WORD ?

START:
    DI
    CLA
    LD #0x8     ;прерывание
    OUT 0x1       ;на ВУ-0
    LD #0x9     ;прерывание
    OUT 3      ;на ВУ-1
    LD #0xA     ;прерывание
    OUT 0x5      ;на ВУ-2
    EI
TIMER_TIME_SET: IN 0x7
    AND #0x40
    BEQ TIMER_TIME_SET
    IN 0x6
    ST $TIME
    LD #0xA
    OUT 0
    JUMP $MAIN

T: WORD ?
COUNT: WORD ?
TEMP: WORD ?

HLTT: HLT

MAIN:
    LD $TIME
    CMP $T
    BEQ MAIN
    LD $TIME
    ST $T
    ST $TEMP
    CLA
    ST $COUNT
    MINUS_60:
    LD $TEMP
    SUB #60
    ST $TEMP
    BMI GOT_MIN
    LD $COUNT
    INC
    ST $COUNT
    JUMP $MINUS_60
    GOT_MIN:
    LD $COUNT
    ADD #0x30
    ST $T3
    LD #0x2B
    ST $T2
    LD $TEMP
    ADD #60
    ST $TEMP
    CLA
    ST $COUNT
    GET_SEC: LD $TEMP
    SUB #10
    ST $TEMP
    BMI GOT_SEC
    LD $COUNT
    INC
    ST $COUNT
    JUMP $GET_SEC
    GOT_SEC: LD $COUNT
    ADD #0x10
    ST $T1
    LD $TEMP
    ADD #10
    ST $T0
    CALL $OUTP0
    LD $TIME
    BEQ HLTT
    JUMP $MAIN


OUTP0:
    CLA
    PUSH
    PUSH
    LD $TS
    BEQ CLEARING
    ASL
    ASL
    ASL
    ASL
    ST &1
    CLEARING: IN 0x15
    AND #0x40
    BEQ CLEARING
    LD &0
    ADD #0xB
    OUT 0x14
    ADD #5
    ST &0
    CMP #0x7D
    BMI CLEARING
    OUTP1: IN 0x15
    AND #0x40
    BEQ OUTP1
    LD $T3
    ADD &1
    OUT 0x14
    OUTP2: IN 0x15
    AND #0x40
    BEQ OUTP2
    LD $T1
    ADD &1
    OUT 0x14
    OUTP3: IN 0x15
    AND #0x40
    BEQ OUTP3
    LD $T0
    ADD &1
    OUT 0x14
    SWAP
    POP
    SWAP
    POP
    RET

DIRECTION: WORD 0xFFFF

INT2:
    NOP
    PUSH
    CLA
    IN 0x4
    CMP #5
    BPL INT0_IRET
    ST $TS
    INT0_IRET: POP
    NOP
    IRET


INT1:
    NOP
    PUSH
    LD $DIRECTION
    NEG
    OUT 2
    ST $DIRECTION
    POP
    NOP
    IRET
    
INT0:
    NOP
    PUSH
    LD #0xA
    OUT 0
    LD $TIME
    ADD $DIRECTION
    ST $TIME
    POP
    NOP
    IRET