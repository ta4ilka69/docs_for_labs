ORG 0x0
V0: WORD $DEFAULT, 0x180
V1: WORD $INT1, 0x180
V2: WORD $DEFAULT, 0x180
V3: WORD $INT3, 0x180
V4: WORD $DEFAULT, 0x180
V5: WORD $DEFAULT, 0x180
V6: WORD $DEFAULT, 0x180
V7: WORD $DEFAULT, 0x180

ORG 0x039
X: WORD 0x0             ; наше X в ячейке памяти 0x039
DEFAULT: IRET
MIN_VALUE: WORD 0xFFEC  ;-20 минимальное значение по ОДЗ
MAX_VALUE: WORD 0x16    ; 22 максимальное значение по ОДЗ
ADDR: WORD $X           ;адрес ячейки X
START:
    DI          ; запрет прерываний
    CLA
    LD #0x9     ; MR1 -> AC (1000|0001 -> 1001)
    OUT 3       ; разрешить прерывание на ВУ-1
    LD #0xB     ; MR3 -> AC (1000|0011 -> 1011)
    OUT 7       ; разрешить прерывания на ВУ-3

T1: WORD ?
PROG: EI        ; разрешить прерывания
    CLA
    INC_LOOP:
        LD $X
        ST $T1
        INC
        CALL $CHECK_X
        PUSH
        LD $T1
        PUSH
        LD $ADDR
        PUSH
        CALL $CAS
        SWAP
        POP
        SWAP
        POP
        SWAP
        POP
        JUMP $INC_LOOP


CHECK_X:
    CMP $MAX_VALUE
    BPL SET_MIN
    CMP $MIN_VALUE
    BMI SET_MIN
    RET
    SET_MIN: 
        LD $MIN_VALUE
        RET

T2: WORD ?
INT1: 
    HLT
    PUSH
    ST $T2
    ADD $T2
    ADD $T2         ;x3
    ASL             ;x3 x2 = x6
    SUB #8
    OUT 2
    POP
    HLT
    IRET

Y3: WORD ?
INT3: 
    HLT
    PUSH
    CLA
    IN 6
    ST $Y3
    CLA
    SUB $Y3
    SUB $Y3
    SUB $Y3
    ADD $X
    ST $X
    POP
    HLT
    IRET

DEREF: WORD ?
CAS: ;PS-0, RET - 1, ADR - 2, OLD_VALUE - 3, FUNC_VALUE - 4
    PUSHF
    DI
    LD &2
    ST $DEREF
    LD &3
    CMP (DEREF)
    BNE OUT_CAS
    LD &4
    ST (DEREF)
    OUT_CAS: POPF
    RET