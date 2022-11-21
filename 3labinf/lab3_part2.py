import re
regfinal = r'([^УЕЫАОЯИЮЭËуёеыаэояию]*[УЕЫАОЯИЮЭËуёеыаэояию][^УЕЫАОЯИЮЭËуёеыаэояию]*){5}\/([^УЕЫАОЯИЮЭËуёеыаэояию]*[УЕЫАОЯИЮЭËуёеыаэояию][^УЕЫАОЯИЮЭËуёеыаэояию]*){7}\/([^УЕЫАОЯИЮЭËуёеыаэояию]*[УЕЫАОЯИЮЭËуёеыаэояию][^УЕЫАОЯИЮЭËуёеыаэояию]*){5}'
regslash = r'.*\/.*\/.*'
for i in range(6):
    fn = './haiku/'+str(i)+'_1.txt'
    s = open(fn,'r',encoding='utf8').readline()
    print("Строка:\n"+s)
    if not re.match(regslash,s):
        print('Не хайку. Должно быть 3 строки')
    else:  
        if re.fullmatch(regfinal,s):
            print('Хайку.')
        else:
            print('Не хайку.')
while True:
    s = input('Enter Haiku-string (print "quit" if you want to quit): ')
    if s == 'quit':
        break
    if not re.match(regslash,s):
        print('Не хайку. Должно быть 3 строки')
    else:  
        if re.fullmatch(regfinal,s):
            print('Хайку.')
        else:
            print('Не хайку.')
    
    