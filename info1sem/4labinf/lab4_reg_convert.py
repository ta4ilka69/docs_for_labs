import re
S = open('./Monday.json', encoding='utf8').readlines()
newlevel = r'.*\{'
newobj = r'\".*\"'
newsimp = r'.*[\,]*'
simple = r'\"[^\"]*\"'
endoflevel = r'.*\}[\,]*'
result = ''
tab = -1
for s in S:
    s = s.rstrip()
    if re.fullmatch(newlevel, s):
        if s != '{':
            result += tab*'  ' + re.findall(newobj, s)[0].replace('"', '')+':'+'\n'
        tab += 1
    elif re.fullmatch(endoflevel, s):
        tab -= 1
        if result[-1] != '\n':
            result += '\n' 
    elif re.match(newsimp, s):
        q = re.findall(simple, s)
        name = q[0]
        value = q[1]
        e = False
        for x in value:
            if x.isalpha():
                e = True
                break
        if e:
            result += tab*'  ' + name.replace('"', '') + ': ' + value.replace('"', '') + '\n'
        else:
            result += tab*'  ' + name.replace('"', '') + ': ' + value.replace('"', '\'') + '\n'
f = open('Monday_reg.yaml', 'w', encoding='utf8')
f.write(result)
f.close()