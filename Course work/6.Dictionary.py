'''
dictionary
----------
'''

d={}
d=dict()
d={'name':'sumanth','course':'pfs','batch':41}
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41}
d={'name':'sumanth','course':'pfs','batch':41,'name':'ajay'}
print(d)#{'name': 'ajay', 'course': 'pfs', 'batch': 41}
d={1:'val',12.3:'val','string':'val',(1,2,3):'val',False:'val'}
print(d)#{1: 'val', 12.3: 'val', 'string': 'val', (1, 2, 3): 'val', False: 'val'}
d['name']='sumanth'
print(d)#{1: 'val', 12.3: 'val', 'string': 'val', (1, 2, 3): 'val', False: 'val', 'name': 'sumanth'}
d={'name':'sumanth','course':'pfs','batch':41,'name':'ajay'}
print(d['name'])#ajay
print(d['course'])#pfs
print(d['batch'])#41
print(d.get('name'))#ajay
print(d.get('age','key is not present'))#key is not present
print(d.get('name','key is not present'))#ajay


d={'name':'sumanth','course':'pfs','batch':41}
d['age']=22
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41, 'age': 22}
d['passedout']=2025
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41, 'age': 22, 'passedout': 2025}
d.update({'phonono':6543218926,'email':'sumanrg@gmail.com'})
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41, 'age': 22, 'passedout': 2025, 'phonono': 6543218926, 'email': 'sumanrg@gmail.com'}
d['passedout']=2026
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41, 'age': 22, 'passedout': 2026, 'phonono': 6543218926, 'email': 'sumanrg@gmail.com'}
d.popitem()
print(d)#
d.pop('age')
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41, 'passedout': 2026 'phonono':6543218926}
del d['phonono']
print(d)#{'name': 'sumanth', 'course': 'pfs', 'batch': 41, 'passedout': 2026}

d={'name':'sumanth','course':'pfs','batch':41,'passedout':2026}
d.keys()
print(d)#dict_values(['name', 'course', 'bacth', 'passedout'])
d.values()
print(d)#dict_values(['sumanth', 'pfs', '41' '2026')]
d.items()
print(d)#{}
d.clear()
print(d)#{}
len(d)
print(len(d))
sorted(d)
print(sorted(d))

d={'name':'sumanth','course':'pfs','batch':41,'passedout':2026}
d.setdefault('age',21)
print(d)


