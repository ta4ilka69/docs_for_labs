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
    DI
    CLA
    LD #0x9     ; MR1 -> AC (1000|0001 -> 1001)
    OUT 3       ; разрешить прерывание на ВУ-1
    LD #0xB     ; MR3 -> AC (1000|0011 -> 1011)
    OUT 7       ; разрешить прерывания на
