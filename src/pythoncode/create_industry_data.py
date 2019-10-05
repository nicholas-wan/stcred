import json
import csv
import codecs
import random
import pickle
import pandas as pd

csvfile = open('../data/lake_data.csv', 'r')

rows = []
fieldnames = ("module_code","course_title","industry","industry_others","occupation","other_occupations_title")
reader = csv.DictReader(csvfile, fieldnames)

i = 0
for row in reader:
    if i != 0:
        datum = dict(row)
        d = {}
        d['ModuleCode'] = datum['module_code']
        d['ModuleTitle'] = datum['course_title']
        d['Industry'] = datum['industry']
        d['Occupation'] = datum['occupation']
        d['TotalEnrolment'] = random.choice(range(50))
        if d['Occupation'] in ['', 'Others, please provide job title and description']:
            d['Occupation'] = datum['other_occupations_title']
        rows.append(d)
    i += 1

rows = rows[:10000]

with open('../data/industry_data.json', 'w') as outfile:
    json.dump(rows, outfile)