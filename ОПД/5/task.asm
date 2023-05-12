ORG 0x1C2
LPART: WORD 0xFF00
RPART: WORD 0x00FF
CHR: WORD 0x0556


START: CLA

WRITING: CALL $CHECK_W1
LD (CHR)
AND $LPART
BEQ STOP
SWAB
OUT 2
CALL $CHECK_W1
LD (CHR)
AND $RPART
BEQ STOP
OUT 2
LD $CHR
INC
ST $CHR
JUMP $WRITING

STOP: HLT

CHECK_W1:
  IN 3
  AND #0x40
  BEQ CHECK_W1
  RET

  
ORG 0x556
CHR12: WORD 0x77BB
CHR34: WORD 0x3231
CHR56: WORD 0x21DA
CHR78: WORD 0x2300
