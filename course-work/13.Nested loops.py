#.Nested loops

#.List

l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    print(i)

for i in l:
    for j in i:
        print(j)
  #or
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])

#.Tuple

t=((1,1),(2,4),(3,9),(4,16),(5,25))
for i in t:
    for j in i:
        print(i,j)


#.nested Dict

data ={
    'apple':{'price':50,'discount':5},
     'mango':{'price':100,'discount':10},
    'papaya':{'price':150,'discount':7},
    'banana':{'price':30,'discount':0},
    }

for i in data:
    for j in data[i]:
        print(data[i][j])

for i in data:
    for j in data[i]:
        print(i,j,data[i][j])

#.List Comprehension

l=[]
for i in range(1,11):
    l.append(i)

print(l)
c=[i for i in range(1,11)]
print(c)

c=[i for i in range(2,101,2)]
print(c)

c=[i**2 for i in range(1,11)]
print(c)

vol='aeiouAEIOU'
sen=input("Enter the sen: ")
res=[]
for i in sen:
    if i in vol:
        res.append(i)
        
print(res)

vol='aeiouAEIOU'
sen=input("Enter the sen: ")
res=[]
for i in sen:
    if i in vol:
        res.append(i)

print(res)
r=[i for i in sen if i in vol]       
print(r)


#.list
vol='aeiouAEIOU'
sen=input("Enter the sen: ")
l=[]
for i in range(5):
    for j in range(5):
        l.append('*')

print(l)
r=['*' for i in range(5) if i%2==0 ]       
print(r)

#.Tuple
t=tuple(i for i in range(10))
s={i  for i in range (10)}
d={i:i*i for i in range(10)}
print(t,s,d,sep='\n')   

t=tuple(i for i in range(10))
s={i  for i in range (10)}
l=[i  for i in range (10)]

d={i:i*i for i in range(10)}
print(t,s,1,d,sep='\n')   

 



    
    
