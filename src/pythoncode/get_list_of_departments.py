import json
import pandas as pd 

data = open("modules_data_v2.json", "r").read()
df = pd.DataFrame(eval(data))
data = df.Department.unique()
data.sort()

result = []
for datum in data:
    d = {"id":datum, "text":datum}
    result.append(d)

with open('departments.json', 'w') as outfile:  
    json.dump(result, outfile)
