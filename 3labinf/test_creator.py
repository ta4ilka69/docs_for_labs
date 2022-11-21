from random import randint


sm = input('Enter the smile: ')
for i in range(5):
    fn = './'+str(i)+'.txt'
    f = open(fn,'w',encoding='utf8')
    l = randint(20,30)
    s = ''
    for i in range(l):
        t = randint(1,7)
        if t==4:
            s+=sm
        elif t==5:
            s+=chr(randint(90,95))
        else:
            s+=chr(randint(1040,1070))
    f.write(s)
    f.close()