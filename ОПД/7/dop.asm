ma E0
mw 0020009001
mw 0010009110
mw 81E6041040
mw 0010809110
mw 0001009021
mw 80E2101040
mw 0010E09001
mw 80C4101040

org 0x10
first_num: word 0xfeb0
res: word ?
start: cla
    ld #-12
    word 0x9010
    st $res
    hlt
end