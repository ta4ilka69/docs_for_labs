import re
S = open('./Monday.json').readlines()
newlevel = r'.*\{'
newobj = r'[^{"]'
simple = r'[^"]*'
endoflevel = r'.*\}'
result = ''
tab = -1
for s in S:
    s.strip()
    if re.fullmatch(newlevel, s):
        tab += 1
        if s!='{':
            result += str(re.fullmatch(newobj,s))+'\n'
    elif re.fullmatch(endoflevel, s):
        tab -= 1
        result +='\n'
    elif re.match(simple, s):
        l = re.match(simple, s)   
