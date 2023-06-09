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