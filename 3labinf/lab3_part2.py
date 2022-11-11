import re
regfinal = r'([^УЕЫАОЯИЮЭËуёеыаэояию]*[УЕЫАОЯИЮЭËуёеыаэояию][^УЕЫАОЯИЮЭËуёеыаэояию]*){5}\/([^УЕЫАОЯИЮЭËуёеыаэояию]*[УЕЫАОЯИЮЭËуёеыаэояию][^УЕЫАОЯИЮЭËуёеыаэояию]*){7}\/([^УЕЫАОЯИЮЭËуёеыаэояию]*[УЕЫАОЯИЮЭËуёеыаэояию][^УЕЫАОЯИЮЭËуёеыаэояию]*){5}'
regslash = r'.*\/.*\/.*'
for i in range(6):
    fn = './tests_for_3lab/'+str(i)+'_1.txt'
    s = open(fn,'r',encoding='utf8').readline()
    print(re.match(regslash,s))
    if not re.match(regslash,s):
        print('Не хайку. Должно быть 3 строки')
    else:  
        if re.match(regfinal,s):
            print('Хайку.')
        else:
            print('Не хайку.')
            

    
    