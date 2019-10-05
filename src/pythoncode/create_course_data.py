import json
import codecs
import random
import pickle

data = json.load(codecs.open('../data/raw_modules_data.json', 'r', 'utf-8-sig'))
keys = data[0].keys()
yearandsems = ['Y17/18-S2','Y17/18-S1','Y16/17-S2','Y16/17-S1','Y15/16-S2','Y15/16-S1','Y14/15-S2','Y14/15-S1','Y13/14-S2','Y13/14-S1','Y12/13-S2','Y12/13-S1','Y11/12-S2','Y11/12-S1']
years = ['2017/2018','2017/2018','2016/2017','2016/2017','2015/2016','2015/2016','2014/2015','2014/2015','2013/2014','2013/2014','2012/2013','2012/2013','2011/2012','2011/2012']
onetwo = ['2','1','2','1','2','1','2','1','2','1','2','1','2','1']
majors = ["Chinese Studies","Communications And New Media","Economics","English Language & Literature","Geography","History","Japanese Studies","Malay Studies","Philosophy","Political Science","Psychology","Social Work","Sociology","Southeast Asian Studies","Dentistry","Biomedical Engineering","Chemical & Biomolecular Engineering","Civil & Environmental Engineering","Electrical & Computer Engineering","Industrial & Systems Engineering","Materials Science And Engineering","Mechanical Engineering","Computing & Engineering","Law","Public Policy","Public Health","Accounting","Decision Sciences","Finance","Human Resource Management Unit","Management And Organisation","Marketing","Strategy And Policy","Computer Science","Information Systems","Information Security","Business Analytics","Architecture","Real Estate","Biological Sciences","Chemistry","Mathematics","Pharmacy","Physics","Statistics & Applied Probability","Medicine","Microbiology & Immunology","Nursing","Pathology","Pharmacology","Physiology","Music"]
with open('topics.pickle', 'rb') as handle:
    topics = pickle.load(handle)

rows = []
for datum in data:
    id = 1
    code = datum['ModuleCode']
    if code in topics:
        for topic in topics[code]:
            s = 'keyword'+str(id)
            id+=1
            datum[s] = topic
    else:
        for k in range(4):
            s = 'keyword'+str(id)
            id+=1
            datum[s] = "NA"
    quotasum = 0
    yearandsem = 'Y18/19-S1'
    if 'CorsBiddingStats' in datum:
        stats = datum['CorsBiddingStats']
        for i in range(len(stats)-1, -1, -1):
            if stats[i]['AcadYear'] == '2018/2019':
                quotasum += min(int(stats[i]['Quota']),int(stats[i]['Bidders']))
        for j in range(len(yearandsems)):
            if quotasum == 0:
                yearandsem = yearandsems[j]
                for i in range(len(stats)-1, -1, -1):
                    if stats[i]['AcadYear'] == years[j] and stats[i]['Semester'] == onetwo[j]:
                        quotasum += min(int(stats[i]['Quota']),int(stats[i]['Bidders']))
        if quotasum == 0:
            quotasum = 0
            yearandsem = ""
    datum['YearSem'] = yearandsem
    # get proportion of enrolment for each batch
    try:
        num = int(datum['ModuleCode'][2])
    except:
        num = int(datum['ModuleCode'][3])
    if num == 1:
        props = [0.45,0.3,0.15,0.1]
    elif num == 2:
        props = [0.3,0.4,0.2,0.1]
    elif num == 3:
        props = [0.05,0.35,0.5,0.1]
    elif num == 4:
        props = [0,0,0.4,0.6]
    sumsumextra = 0
    for i in range(len(props)):
        totalenrolment = int(quotasum * props[i])
        sumextra = 0
        for j in range(3):
            datumcopy2 = datum.copy()
            datumcopy2['Major'] = random.choice(majors)
            extra = random.choice(range(20))
            sumextra += extra
            datumcopy2['TotalEnrolment'] = totalenrolment + extra
            datumcopy2['Year'] = "Year " + str(i+1)
            rows.append(datumcopy2)
        datumcopy = datum.copy()
        datumcopy['Year'] = "Year " + str(i+1)
        datumcopy['TotalEnrolment'] = totalenrolment + sumextra
        datumcopy['Major'] = "All"
        rows.append(datumcopy)
        sumsumextra += sumextra
    datumcopy3 = datum.copy()
    datumcopy3['Year'] = "All"
    datumcopy3['Major'] = "All"
    datumcopy3['TotalEnrolment'] = int(quotasum) + sumsumextra
    rows.append(datumcopy3)

rows = rows[:10000]

with open('../data/course_data.json', 'w') as outfile:
    json.dump(rows, outfile)