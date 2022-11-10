import re
sm = input('Enter the smile for search: ')
sr = re.escape(sm)
for i in range(5):
    fn = './tests_for_3lab/'+str(i)+'.txt'
    s = open(fn, 'r', encoding='utf8').readline()
    print("Строка:\n")
    print(s)
    # Not using regexp
    print('Test '+str(i+1)+': '+str(s.count(sm)))
    # Using regexp
    print('Test '+str(i+1)+' using regexp: ' +
          str(len(re.findall(sr, s))))