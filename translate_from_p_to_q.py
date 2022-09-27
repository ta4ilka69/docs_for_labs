global Alphabet
Alphabet = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ'


def from_p_to_q(p, q, n):
    return from_10_to_q(q, from_p_to_10(p, n),)


def from_10_to_q(q, n):
    s = ''
    n = int(n)
    while n != 0:
        s = Alphabet[n % q] + s
        n = n//q
    return (s)


def from_p_to_10(p, n):
    n = str(n)
    out = 0
    for i in range(len(n)):
        out += (Alphabet.index(n[len(n)-i-1]))*p**i
    return (out)


def check(p, q, n):
    if not (p.isnumeric) or not (q.isnumeric) or float(p) > 36 or float(q) > 36 or float(p) < 2 or float(q) < 2 or int(float(p)) != float(p) or int(float(q)) != float(q):
        return False
    p = int(float(p))
    for i in range(p, len(Alphabet)):
        if Alphabet[i] in n:
            return False
    for i in range(len(n)):
        if n[i] not in Alphabet:
            return False
    return True


def Fib_CC(n):
    if n==0:
        return 0
    a = [1, 2]
    while a[-1] <= n:
        a.append(a[-1]+a[-2])
    out = ''
    for i in range(len(a)-1, -1, -1):
        if a[i] <= n:
            out += '1'
            n -= a[i]
        else:
            out += '0'
    return out


s = ''
while s != '1' and s != '2':
    s = input(
        'Выберите режим:\n 1. CC c целыми основаниями p,q ∈ [2;36] \n 2. СС Цекендорфа (фибоначчиева СС)\n (Введите 1 или 2)\n')
if s == '1':
    S = input(
        'Введите через пробел начальное основание СС, конечное и само число\n').split()
    if len(S) != 3:
        print("Неверный формат ввода!")
    else:
        p, q, n = map(str, S)
        if check(p, q, n):
            p = int(float(p))
            q = int(float(q))
            n = int(n)
            print(from_p_to_q(p, q, n))
        else:
            print('Проверьте возможность существования числа в заданных СС')
else:
    s = input(
        'Введите число в десятичной системе счисления, чтобы перевести его в СС Цекендорфа:\n')
    if s.isnumeric() and int(s)==float(s) and int(s)>=0:
        print(int(Fib_CC(int(s))))
    else:
        print("Неверный формат ввода!")
