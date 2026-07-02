import csv
import re

def to_number(s):
    s = re.sub(r'[^\d,]', '', s)    
    if s == '':                      
        return 0.0
    return float(s.replace(',', '.'))

def first_upper(s):
    return s[0].upper() + s[1:].lower()



result = []
f = open("problem.txt", encoding="utf-8")
for index, line in enumerate(f):
    line = re.sub('контрагент', 'contractor', line ,flags=re.IGNORECASE); line = re.sub('договор', 'contract_num', line ,flags=re.IGNORECASE)
    line = re.sub('объект', 'object_name', line ,flags=re.IGNORECASE); line = re.sub('расходы', 'expenses', line ,flags=re.IGNORECASE)
    line = re.sub('выручка', 'revenue', line ,flags=re.IGNORECASE); line = re.sub(' от ', '; date: ', line ,flags=re.IGNORECASE)
    line = line.replace('|', ' ; ').replace(':', ' ')
    line = line.split(';')
    print (line)
    dictt = {}
    for object in line:
        object = object.strip()
        if ' ' not in object:
            continue
        name, value = object.split(' ', 1)
        value = "".join(value).strip()

        dictt[name] = value 
    
    dictt['contractor'] = first_upper(dictt['contractor'])
    result.append(dictt)
    

with open('data.csv', 'w', newline = "", encoding = "utf-8-sig") as csvfile:
    for d in result:
        revenue  = float(to_number(d['revenue']))
        expenses = float(to_number(d['expenses']))
        d['expenses'] = str(round(expenses,2))
        d['revenue'] = str(round(revenue,2))
        d['profit'] = str(round(revenue - expenses, 2))
    writer = csv.DictWriter(csvfile, fieldnames=result[0].keys())
    writer.writeheader()
    writer.writerows(result)


print (result)
        


        
        



