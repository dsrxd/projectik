import csv
from itertools import *
import re

def to_number(s):
    s = re.sub(r'[^\d,]', '', s)    
    if s == '':                      
        return 0.0
    return float(s.replace(',', '.'))

def first_upper(s):
    return s[0].upper() + s[1:]

def block2(s):
    new_s = s.group(1)
    if new_s.lower().startswith('дог.'):
        return '[дог.' + new_s[4:].upper() + ']'
    return '[' + new_s.upper() + ']'

exc = ['им', "бывш", "дог"]

def block3(s):
    new_s = s.group()
    if new_s.lower() in exc:
        return new_s.lower()
    return new_s[0].upper() + new_s[1:]

def normalizer(s):
    
    s = re.sub(r'^(\S+)', lambda m: m.group(1).upper(), s)

    s = re.sub(r'\[([^\]]+)\]', block2, s)

    s = re.sub(r'[а-яёa-z]+', block3, s)

    return s

def normalize_numbers(s):
    
    
    return


result = []
f = open("problem.txt", encoding="utf-8")
for index, line in enumerate(f):
    line = line.lower().replace('контрагент', ' contractor ').replace('договор', " contract_num ").replace('объект', " object_name ")\
        .replace('расходы',  " expenses ").replace('выручка', " revenue ").replace(" от ", '; date: ').replace("|", " ; ")\
            .replace(':', " ").split(';')\
        
    dictt = {}
    for object in line:
        object = object.strip()
        if ' ' not in object:
            continue
        name, value = object.split(' ', 1)
        value = "".join(value).strip()

        dictt[name] = value

    dictt['contract_num'] = dictt['contract_num'].upper()
    dictt['object_name'] = normalizer(dictt['object_name'])
    dictt['contractor'] = first_upper(dictt['contractor'])
    result.append(dictt)

with open('data.csv', 'w', newline = "", encoding = "utf-8-sig") as csvfile:
    for d in result:
        revenue  = float(to_number(d['revenue']))
        expenses = float(to_number(d['expenses']))
        d['expenses'] = str(round(float(to_number(d['expenses'])),2))
        d['revenue'] = str(round(float(to_number(d['revenue'])),2))
        d['profit'] = str(round(revenue - expenses, 2))
    writer = csv.DictWriter(csvfile, fieldnames=result[0].keys())
    writer.writeheader()
    writer.writerows(result)



# with open('data.csv', 'a', newline='', encoding="utf-8-sig") as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=['profit'])
#     writer.writeheader()
#     for d in result:
#         revenue  = float(d['revenue'].replace(',', '.').replace(' ', ''))
#         expenses = float(d['expenses'].replace(',', '.').replace(' ', ''))
#         d['profit'] = str(round(revenue - expenses, 2))


#     writer.writerows()

print (dictt.keys())   
print (result, end='\n')
print (dictt.values())
        


        
        



