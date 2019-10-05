import json
import codecs

data1 = json.load(codecs.open('modules1.json', 'r', 'utf-8-sig'))
data2 = json.load(codecs.open('modules2.json', 'r', 'utf-8-sig'))

keys = data1[0].keys()

rows = []
existed = {}
for i in range(len(data1)):
    if data1[i]['ModuleCode'] not in existed:
        existed[data1[i]['ModuleCode']] = 1
        d = {}
        for key in keys:
            if key in data1[i]:
                d[key] = data1[i][key]
        rows.append(d)
    if data2[i]['ModuleCode'] not in existed:
        existed[data2[i]['ModuleCode']] = 1
        d = {}
        for key in keys:
            if key in data2[i]:
                d[key] = data2[i][key]
        rows.append(d)

with open('modules_data.json', 'w') as outfile:
    json.dump(rows, outfile)
