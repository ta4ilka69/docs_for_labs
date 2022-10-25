from random import randint


sm = ':-{\\'
for i in range(5):
    fn = './tests_for_3lab/'+str(i)+'.txt'
    f = open(fn,'w',encoding='utf8')
    l = randint(20,100)
    s = ''
    for i in range(l):
        t = randint(1,6)
        if t==4:
            s+=sm
        else:
            s+=chr(randint(1040,1104))
    f.write(s)
    f.close()