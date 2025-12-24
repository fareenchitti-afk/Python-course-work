#. Lambda functions

def wish(name):
    print(f'Welcome to python{name}')
wish("Fareen")
wish("Priya")
wish("Rama")

wish=lambda name: f'Welcome to python (name)!'
print(wish("Fareen"))
print(wish("Priya"))
print(wish("Rama"))

#.2
def sq(n):
    print(f'squares of a numbers is (n*n)')
sq(6)

lsq=lambda n: f'squares of a numbers is (n*n)'
print(sq(7))

#.3
add=lambda a,b:a+b
print(add(7,3))

#.4

a=lambda r:3.14*r*r
print(a(15))
print(a(5))
#.5

eord=lambda n:"even" if n%2==0 else "odd"
print(eord(7))

#.6
v='aeiouAEIOU'
vc=lambda ch:"vowel" if ch in v else "con"
print(vc("a"))

#.7

l=[1,2,3,4,5]
names=['shaik fareen','rama reddy','krishna priya']
price=[20000,38000,44000]

res=list(map(lambda i:f'{i}%',l))
res1=list(map(lambda i: i.title(),names))
res2=list(map(lambda i: f'${i+i*0.18}',price))

print(res)
print(res1)
print(res2)

#.8
l=[1,2,3,4,5]
names=['shaik fareen','rama reddy','krishna priya']
price=[20000,38000,44000]
products={
    'milk':20,
    'bread':10,
    'salt':30,
    'eggs':0,
    'sugar':5,
    'soap':0,
    'chill powder':1,
    'biscuts':0,
    'dates':2
    }
res=list(filter(lambda i:i%2==0,l))
res1=list(filter(lambda i: i[0]=='s',names))
res2=list(filter(lambda i: i>35000,price))
res3=list(filter(lambda i: products[i]==0,products))

print(res)
print(res1)
print(res2)
print(res3)


#.9
from functools import reduce

l=[1,2,3,4,5]
lang=['java','python','javascript','csharp','ruby']

res=reduce(lambda a,b:a*b,l)
res1=reduce(lambda a,b: a+','+b, lang)

print(res)
print(res1)


#.10

d={
    'fareen':80,
    'rama':67,
    'priya':54,
    'reddy':96,
    'devi':84
    }

print(dict(sorted(d.items(),key= lambda i:i[0])))
print(dict(sorted(d.items(),key= lambda i:i[0],reverse=True)))

print(dict(sorted(d.items(),key= lambda i:i[1])))
print(dict(sorted(d.items(),key= lambda i:i[1],reverse=True)))







      




