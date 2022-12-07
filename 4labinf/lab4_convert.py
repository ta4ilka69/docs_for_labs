f = open('./test.json', 'r', encoding='utf-8')
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
mastab = [-3]
while i < len(s):
    if mastab[-1] == tab:
        name = False
    if s[i] == '[':
        i += 1
        mas = True
        if mastab[-1]==-3:
            mastab[-1] = tab
        else:
            mastab.append(tab)
        name = False
        result += '\n'
    if s[i] == '{':
        tab += 1
        if not(mas and tab - mastab[-1]<2):
            name = True
        i += 1
        if tab != 0:
            if result[-1] != '\n':
                result += '\n'
    elif s[i] == '\"':
        if name:
            t = ''
            i += 1
            while s[i] != '\"':
                t += s[i]
                i += 1
            i += 1
            if mas and tab == mastab[-1]:
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
                if mas and mastab[-1] == tab:
                    if result[-1] != '\n':
                        result += '\n'
                    result += mastab[-1]*'  '+'- '+"\'"+t+"\'"
                else:
                    result += "\'"+t+"\'"
                    name = True
            else:
                if mas and tab - mastab[-1]<2:
                    if result[-1] != '\n':
                        result += '\n'
                    result += mastab[-1]*'  '+'- '+t
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
        if len(mastab)==1:
            mas = False
        i += 1
        name = True
        if len(mastab)==1:
            mastab[-1]=-3
        else:
            del(mastab[-1])
    elif s[i].isdigit():
        t = ''
        while s[i].isdigit():
            t += s[i]
            i += 1
        if mas and mastab[-1] == tab:
            if result[-1] != '\n':
                result += '\n'
            result += mastab[-1]*'  '+'- '+t
        else:
            result += t
    elif s[i].isalpha():
        t = ''
        while s[i].isalpha():
            t += s[i]
            i += 1
        if mas and mastab[-1] == tab:
            if result[-1] != '\n':
                result += '\n'
            result += mastab[-1]*'  '+'- '+t
        else:
            result += t
    else:
        i += 1
f = open("./test.yaml", 'w', encoding='utf-8')
f.write(result)
f.close()
