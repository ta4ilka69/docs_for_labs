import re

s = input().split()
letterRow1 = r'(?i)(\w\w)'
letterRow2 = r'(?i)\w(\w\w)'

for t in s:
    k = re.findall(letterRow1, t.lower())
    k2 = re.findall(letterRow2, t.lower())
    q = False
    for y in k:
        if y[0]==y[1]:
            print(t)
            q = True
            break
    if not(q):
        for y in k2:
            if y[0]==y[1]:
                print(t)
                break
            