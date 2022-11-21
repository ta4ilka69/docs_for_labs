import re
sm = input('Enter the smile for search: ')
sr = re.escape(sm)
for i in range(5):
    fn = './'+str(i)+'.txt'
    s = open(fn, 'r', encoding='utf8').readline().strip()
    print("Строка:")
    print(s)
    # Not using regexp
    print('Test '+str(i+1)+': '+str(s.count(sm)))
    # Using regexp
    print('Test '+str(i+1)+' using regexp: ' +
          str(len(re.findall(sr, s))))
while True:
    s = input('Enter string with smile for search (print "quit" if you want to quit): ')
    if s == 'quit':
        break
    print("Count of smiles in string: "+str(len(re.findall(sr, s))))