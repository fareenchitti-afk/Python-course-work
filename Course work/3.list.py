# List operations program

l=[]
l=list()
l=[1,2,3,4,5,6]
l=list([1,2,3,4,5])
print(l)#[1, 2, 3, 4, 5]
l=[[1,2],[3,4],[5,6]]
l=[1,1,1,1,1,1,2]
print(l)#[1, 1, 1, 1, 1, 1, 2]

print( [1,2,3]+[4,5,6])#[1, 2, 3, 4, 5, 6]

print([1,2]*5)#[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

print(l)#[1, 1, 1, 1, 1, 1, 2]

print( 2 in l)#True

print( 6 in l)#False

l=['Fareen','Haseena','Mahaboob','Farhana','Fazil','Hussain','Saheb']

print(l)#['Fareen', 'Haseena', 'Mahaboob', 'Farhana', 'Fazil', 'Hussain', 'Saheb']

print(l[2])#Mahaboob

print(l[-3])#Fazil

print(l[-2])#Hussain

print(l[-1])#Saheb

print(l[1])#Haseena

print(l[0])#Fareen

print(l[1:3])#['Haseena', 'Mahaboob']

print(l[-1:-4:-1])#['Saheb', 'Hussain', 'Fazil']

print(l[::2])#['Fareen', 'Mahaboob', 'Fazil', 'Saheb']

print(l[1::2])#['Haseena', 'Farhana', 'Hussain']

print(l[::-1])#['Saheb', 'Hussain', 'Fazil', 'Farhana', 'Mahaboob', 'Haseena', 'Fareen']


l=[[1,2],[3,4],[5,6]]
print(l[2])#[5, 6]
print(l[1])#[3, 4]
print(l[0])#[1, 2]
print(l[0][0])#1
print(l[2][0])#5
print(l[1][1])#4

l=[10,20,30,40,50]

print(id(l))#2266115977536
print(l[1])#20
l[1]=20.3
print(l)#[10, 20.3, 30, 40, 50]
print(id(l))#2266115977536
l[2]=30+4j
print(l)#[10, 20.3, (30+4j), 40, 50]
l[3]='string'
print(l)#[10, 20.3, (30+4j), 'string', 50]

l
[10, 20.3, (30+4j), 'string', 50]

l.append([1,2,3])
print(l)#[10, 20.3, (30+4j), 'string', 50, [1, 2, 3]]
l.append((10,202,30))
print(l)#[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30)]
print(l)#[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30)]
l.append(70)
l.append(80)
print(l)#[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30), 70, 80]
l.extend([100,90,20,10])
print(l)#[10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.insert(0,10)
print(l)#[10, 10, 20.3, (30+4j), 'string', 50, [1, 2, 3], (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.insert(5,{1:2,2:4,3:6,4:8})
print(l)#[10, 10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.insert(8,{1,2,3,4})
print(l)#[10, 10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, (10, 202, 30), 70, 80, 100, 90, 20, 10]


l
[10, 10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.remove(10)
print(l)#[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, (10, 202, 30), 70, 80, 100, 90, 20, 10]
l.remove((10, 202, 30))
print(l)#[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], {1, 2, 3, 4}, 70, 80, 100, 90, 20, 10]
l.remove({1, 2, 3, 4})
print(l)#[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 100, 90, 20, 10]
l.remove(100)
print(l)#[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]


l
[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]

l.pop(2)
(30+4j)
print(l)#[10, 20.3, (30+4j), 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop(1)#[10, 20.3, 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
20.3
print(l)#[10, 'string', {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]
l.pop(1)
'string'
print(l)#[10, {1: 2, 2: 4, 3: 6, 4: 8}, 50, [1, 2, 3], 70, 80, 90, 20, 10]

l.pop(1)
{1: 2, 2: 4, 3: 6, 4: 8}
l
[10, 50, [1, 2, 3], 70, 80, 90, 20, 10]
print(l.pop())#10
print(l)#[10, 50, [1, 2, 3], 70, 80, 90, 20]
print(l.pop())#20
print(l.pop())#90
print(l.pop())#80
print(l)#[10, 50, [1, 2, 3], 70]
del l[2]
print(l)#[10, 50, 70]


l.clear()
print(l)#[]
l=[1,2,3,4]
l.clear()
print(l)#[]
l=[10,20,30,40,50,60,70,80]
print(l.index(30))#2
print(l.index(80))#7


l=[10, 20, 30, 40, 50, 60, 70, 80]
l.append(10)
print(l)#[10, 20, 30, 40, 50, 60, 70, 80, 10]
print(l.index(10))#0
print(l.count(10))#2
l.sort()
print(l)#[10, 10, 20, 30, 40, 50, 60, 70, 80]

l=[8,2,3,4,1,8,3,4]

print(sorted(l))#[1, 2, 3, 3, 4, 4, 8, 8]

print(l)#[8, 2, 3, 4, 1, 8, 3, 4]
l.sort()
print(l)#[1, 2, 3, 3, 4, 4, 8, 8]
l.sort(reverse=True)
print(l)#[8, 8, 4, 4, 3, 3, 2, 1]
l.reverse()
print(l)#[1, 2, 3, 3, 4, 4, 8, 8]
a=[1,2,3,4,5]
print(a)#[1, 2, 3, 4, 5]
b=a
print(b)#[1, 2, 3, 4, 5]
b.append(6)
print(b)#[1, 2, 3, 4, 5, 6]
print(a)#[1, 2, 3, 4, 5, 6]9
c=a.copy()
print(c)#[1, 2, 3, 4, 5, 6]
c.append(9)#[1, 2, 3, 4, 5, 6, 9]
print(c)#[1, 2, 3, 4, 5, 6]
print(a)#[1, 2, 3, 4, 5, 6]

l
[1, 2, 3, 3, 4, 4, 8, 8]
print(max(l))#8
print(min(l))#1
print(len(l))#8
l=[0,0.0,'',[],(),{},set(),False]
print(any(l))#False
print(all(l))#False

l.append(1)
print(l)#[0, 0.0, '', [], (), {}, set(), False, 1]
print(any(l))#True
print(all(l))#Flase
a
[1, 2, 3, 4, 5, 6]
print(all(a))#True


