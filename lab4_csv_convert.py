import json, csv
js = json.loads(open('./Monday_cs.json',encoding='utf8').read())
wr = csv.writer(open('./Monday_cs.csv','w',encoding='utf8'),delimiter=',',skipinitialspace=False)
headers = []
for x in js:
    headers.append(x)
columns = ['']+list(js[headers[0]].keys())
wr.writerow(columns)
for i in range(len(headers)):
    t = [headers[i]]
    for j in range(1,len(columns)):
        t.append(js[headers[i]][columns[j]])
    wr.writerow(t)