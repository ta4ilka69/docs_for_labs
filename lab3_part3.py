import re
# Буквы К Р Т; расстояние 1
reg = r'[^крт]*к[^крт]р[^крт]т[^крт]*'
S = open('./tests_for_3lab/0_3.txt', 'r', encoding='utf8').readlines()
for s in S:
    s = s.strip()
    if bool(re.fullmatch(reg, s)):
        print(s)