import re
q = input('Enter 3 letters and distance: ')
q = list(q.split())
if len(q)!=4:
    print('Incorrect input: 3 letters and distance')
elif not q[3].isdigit():
    print('Incorrect input: distance is not a number')
else:
    l = int(q[3])
    w = q[0]
    e = q[1]
    y = q[2]
    treg = fr'[^{w}{e}{y}]*{w}([^{w}{e}{y}]){{{l}}}{e}([^{w}{e}{y}]){{{l}}}{y}[^{w}{e}{y}]*'
    reg = re.compile(treg)
    S = open('./tests_for_3lab/0_3.txt', 'r', encoding='utf8').readline()
    for s in S.split():
        if bool(re.fullmatch(reg.pattern, s)):
            print(s)