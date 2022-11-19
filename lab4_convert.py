f = open('./Monday.json', 'r', encoding='utf-8')
F = f.readlines()
f.close()
s = ''
for S in F:
    s += S.strip()
result = ''
tab = -1
i = 0
name = True
mas = False
mastab = -2
while i < len(s):
    if s[i] == '[':
        i += 1
        mas = True
        mastab = tab
    if s[i] == '{':
        tab += 1
        name = True
        i += 1
        if tab != 0:
            result += '\n'
    elif s[i] == '\"':
        if name:
            t = ''
            i += 1
            while s[i] != '\"':
                t += s[i]
                i += 1
            i += 1
            if mas and tab == mastab:
                result += "  "*tab + '- ' + t
            else:
                result += "  "*tab + t
            name = False
        else:
            t = ''
            i += 1
            while s[i] != '\"':
                t += s[i]
                i += 1
            i += 1
            q = True
            for x in t:
                if x.isalpha():
                    q = False
                    break
            if q:
                result += "\'"+t+"\'"
            else:
                result += t
            name = True
    elif s[i] == ':':
        result += ': '
        i += 1
    elif s[i] == ',':
        result += '\n'
        i += 1
    elif s[i] == '}':
        tab -= 1
        i += 1
    elif s[i] == ']':
        mas = False
        i += 1
    else:
        i += 1
f = open("./Monday.yaml", 'w', encoding='utf-8')
f.write(result)
f.close()
