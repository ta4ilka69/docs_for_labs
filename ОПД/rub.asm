ORG 0x0010
first_element: word 0x1000
word 0x0023
word 0x1000
word 0x0022
word 0x2000
word 0x0023

count: word 0x0006

res_lower: word ?
res_upper: word ?

start_mas: word $first_element

index_lower: word ?
index_upper: word ?

start:
CLA
LD $start_mas
ST $index_lower
INC
ST $index_upper
adding_loop: 
CLC
LD (index_lower)
ADD $res_lower
ST $res_lower
LD (index_upper)
ADC $res_upper
ST $res_upper
LD $index_lower
ADD #2
ST $index_lower
LD $index_upper
ADD #2
ST $index_upper
SUB $start_mas
CMP $count
BPL ending
JUMP $adding_loop
ending: CLA
ST $count
HLT

making_MODULE_x: ;0-ret, 1-num
    mask_last_bit: word 0x1000 ;13-й бит
    mask_others: word 0x0FFF; все биты, младше 13 (т.е. без знакового бита)
    ld &1
    and $mask_last_bit
    beq plus
    minus:
    ld &1
    neg
    and $mask_others
    st &1
    plus:
    ld &1
    RET

check_if_lower: ;0-ret, 1 - модуль числа (для вычитания)
    ld $res_lower
    cmp &1
    BPL RETURN
    ld $res_upper
    dec
    st $res_upper
    RETURN: ret