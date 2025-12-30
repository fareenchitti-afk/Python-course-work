#.regular expressions

import re
s='python programming'
pattern=r'[0-9A-Za-z]' #.raw expression
res= re.match(pattern,s)
print(res.group())

import re
s='1python programming'
pattern=r'[0-9A-Za-z_]' #.raw expression
res= re.match(pattern,s)
print(res.group() if res else "Not found")


#.search

import re
s='python version 13.0'
pattern=r'\d'
res= re.search(pattern,s)
print(res.group())


import re

s='12.0 3456 6789 13.0'
pattern=r'\d{4}'
res= re.search(pattern,s)
print(res.group())


#.Find all

s='cd10 asdbgvfv 1234 12.0 14.00 vbjhgfyuyg cd02'
pattern=r'\d{2}'
res= re.findall(pattern,s)
print(res)
#.print(res.group() if res else "not found

#.findeiter

s='cd10 asdbgvfv 1234 12.0 14.00 vbjhgfyuyg cd02'
pattern=r'\d{2}'
res= re.finditer(pattern,s)
#.print(res)
for i in res:
    print(i.start(),i.group() if i else "Not found")

#.spliting

s='python,java;c++:javascript#html'
pattern='[,;:#]'
res=re.split(pattern,s)
print(res)

#.repacement

s='sa12 ro99 gh120 bu93'
res= re.sub(r'[aeiouAEIOU] {1}','*',s)
print(res)

#.Meta charecters

s='cat cot cut sit rat rod hit hut husky'
res=re.findall(r'r.t',s)
print(res)

s='Today is monday it fells very hard to go to class'
res=re.findall(r'^[A-Z]',s)
print(res)

s='Today is monday it fells very hard to go to class'
res=re.findall(r'[a-z]&',s)
print(res)

s='p py pyvvl pyvvvl pyvvvvvl'
res=re.findall(r'pyv+',s)
print(s)

s='p py pyvvl pyvvvl pyvvvvvl'
res=re.findall(r'pyv*',s)
print(s)

s='cat ct'
res=re.findall(r'cat',s)
print(res)

s='cat ct'
res=re.findall(r'c?t',s)
print(res)

s='ct cot coot'
res=re.findall(r'c.?.t',s)
print(res)

s='Fareen05 Ramareddy51 Priya11 Ajay18 Satish12'
res=re.findall(r'[a-z]{3}',s)
print(res)


