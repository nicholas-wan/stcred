import json
import codecs
import random
import pickle

data = json.load(codecs.open('../data/raw_modules_data.json', 'r', 'utf-8-sig'))
keys = data[0].keys()

yearandsems = ['Y17/18-S2','Y17/18-S1','Y16/17-S2','Y16/17-S1','Y15/16-S2','Y15/16-S1','Y14/15-S2','Y14/15-S1']
majors = ["Chinese Studies","Communications And New Media","Economics","English Language & Literature","Geography","History","Japanese Studies","Malay Studies","Philosophy","Political Science","Psychology","Social Work","Sociology","Southeast Asian Studies","Dentistry","Biomedical Engineering","Chemical & Biomolecular Engineering","Civil & Environmental Engineering","Electrical & Computer Engineering","Industrial & Systems Engineering","Materials Science And Engineering","Mechanical Engineering","Computing & Engineering","Law","Public Policy","Public Health","Accounting","Decision Sciences","Finance","Human Resource Management Unit","Management And Organisation","Marketing","Strategy And Policy","Computer Science","Information Systems","Information Security","Business Analytics","Architecture","Real Estate","Biological Sciences","Chemistry","Mathematics","Pharmacy","Physics","Statistics & Applied Probability","Medicine","Microbiology & Immunology","Nursing","Pathology","Pharmacology","Physiology","Music"]
types = ["Core Module","Programme Electives","GEM","UE"]
weightages = [[10,20,30,40],[20,30,40,10],[30,40,10,20],[40,10,20,30],[0,20,40,40],[0,40,20,40],[0,0,50,50],[20,0,60,20],[10,0,30,60],[0,0,50,50],[30,0,0,70]]
yesnos = ["Yes", "Yes", "Yes", "Yes", "No"]
rows = []

for datum in data:
    d = {}
    code = datum['ModuleCode']
    d['ModuleCode'] = code
    d['ModuleTitle'] = datum['ModuleTitle']
    d['YearSem'] = random.choice(yearandsems)
    d['Department'] = datum['Department']
    weightage = random.choice(weightages)
    d['Assignments'] = weightage[0]
    d['Class Participation'] = weightage[1]
    d['Project Work'] = weightage[2]
    d['Exams'] = weightage[3]

    try:
        d['ModuleDescription'] = datum['ModuleDescription']
    except:
        pass
        
    if code[:2] == "LA":
        d['Type'] = "Language Module"
    else:
        d['Type'] = random.choice(types)    

    try:
        workload = datum['Workload'].split("-")
    except:
        workload = ["0","0","0","0","0"]
    if len(workload) != 5:
        workload = ["NA","NA","NA","NA","NA"]
    d['Lecture'] = workload[0]
    d['Tutorial'] = workload[1]
    d['Lab'] = workload[2]
    d['Project'] = workload[3]
    print(workload)
    d['Preparation'] = workload[4]
    d['Graded'] = random.choice(yesnos)

    enrolmentsum = 0
    for i in range(3):
        d1 = d.copy()
        d1['Major'] = random.choice(majors)
        enrolment = random.choice(range(30))
        enrolmentsum += enrolment
        d1['TotalEnrolment'] = enrolment
        rows.append(d1)
    
    d['Major'] = "All"
    d['TotalEnrolment'] = enrolmentsum
    rows.append(d)

rows = rows[:10000]

with open('../data/module_type_data.json', 'w') as outfile:
    json.dump(rows, outfile)