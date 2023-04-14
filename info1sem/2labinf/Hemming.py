#Проверка исходного кода на соответствие коду Хэмминга длиной 7 бит
def check(s):
    if len(s)!=7:
        return False
    if s.count('1')+s.count('0')!=7:
        return False
    return True
    
#Функция поиска ошибки и её исправления
def Hemming(s):
    s1 = 0
    for i in range(0,len(s),2):
        s1+=int(s[i])
    s1 = s1%2
    s2 = sum(map(int, [s[1],s[2],s[5],s[6]]))%2
    s3 = sum(map(int,[s[3],s[4],s[5],s[6]]))%2
    k = int(str(s3)+str(s2)+str(s1),2)
    if k == 0:
        print('Всё верно!')
    else:
        print('Ошибка в бите под номером '+str(k))
    print('Правильное сообщение: ', end='')
    if k!=3:
        print(s[2],end='')
    else:
        print(int(not(bool(s[2]))),end='')
    if k!=5:
        print(s[4],end='')
    else:
        print(int(not(bool(s[4]))),end='')
    if k!=6:
        print(s[5],end='')
    else:
        print(int(not(bool(s[5]))),end='')
    if k!=7:
        print(s[6],end='')
    else:
        print(int(not(bool(s[6]))),end='')
    



s = input('Введите код Хэмминга длиной 7 бит:\n')
if check(s):
    Hemming(s)
else:
    print('Проверьте, что код состоит из символов 0 и 1 и длиной 7')