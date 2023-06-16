import random
a = ["Артем", "Фаридун", "Валера", "Ваня Ф", "Ваня П", "Анар","Андрей"]
b = []
while len(b)!=len(a):
    c = random.randint(1,len(a))
    if c not in b:
        b.append(c)
for i in range(len(a)):
    print(str(a[i])+": " + str(b[i]))