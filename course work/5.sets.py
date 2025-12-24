'''
Set
------
'''
s=set()
print(s)#set()
s={1,2,3,4,5,6,7}
print(s)#{1, 2, 3, 4, 5, 6, 7}
s={1,1,1,2,12,3,4,5,5,1,12,3}
print(s)#{1, 2, 3, 4, 5, 12}

#.Set properties
s={100,4000,1,2,57,12,45,18,57}
print(s)#{4000, 1, 2, 100, 12, 45, 18, 57}
s.add(90)
print(s)#{4000, 1, 2, 100, 12, 45, 18, 57, 90}
s.remove(4000)
print(s)#{1, 2, 100, 12, 45, 18, 57, 90}
s.add(1234)
print(s)#{1, 2, 100, 12, 45, 18, 1234, 57, 90}
s.add(12+7j)
print(s)#{1, 2, (12+7j), 100, 12, 45, 18, 1234, 57, 90}
s.add(False)
print(s)#{False, 1, 2, (12+7j), 100, 12, 45, 18, 1234, 57, 90}
s.add(True)
print(s)#{True,False, 1, 2, (12+7j), 100, 12, 45, 18, 1234, 57, 90}
s.add(None)
print(s)#{False, 1, 2, (12+7j), 100, None, 12, 45, 18, 1234, 57, 90}
s.add((1,2,3,4))
print(s)#{False, 1, 2, (12+7j), 100, None, 12, 45, True,(1, 2, 3, 4), 18, 1234, 57, 90}

#.Operations on sets

girls={'fareen','ruchitha', 'preethi', 'varsha','rama','priya','bindu'}
guys={'fazil','hussain','mahaboob','amaan','abbu','ahaan','ahil'}
guys.add('kalyan')
online={'kalyan','pawan',}
print(girls)#{'fareen', 'priya', 'bindu', 'rama', 'varsha', 'preethi', 'ruchitha'}
print(guys)#{'amaan', 'abbu', 'hussain', 'kalyan', 'mahaboob', 'ahil', 'ahaan', 'fazil'}
print(online)#{'pawan', 'kalyan'}
print('fareen' in girls)#True
print('ahil' in guys)#True
print(girls | guys)#{'fareen', 'hussain', 'bindu', 'kalyan', 'ahil', 'preethi', 'ahaan', 'amaan', 'abbu', 'priya', 'rama', 'mahaboob', 'varsha', 'ruchitha', 'fazil'}
print(girls.union(guys))#{'fareen', 'hussain', 'bindu', 'kalyan', 'ahil', 'preethi', 'ahaan', 'amaan', 'abbu', 'priya', 'rama', 'mahaboob', 'varsha', 'ruchitha', 'fazil'}

print(online.intersection(guys))#{'kalyan'}

print(guys.difference(online))#{'hussain', 'ahil', 'ahaan', 'amaan', 'abbu', 'mahaboob', 'fazil'}
print(guys.symmetric_difference(online))#{'hussain', 'ahil', 'ahaan', 'amaan', 'abbu', 'pawan', 'mahaboob', 'fazil'}
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.symmetric_difference(b))#{1, 2, 3, 6, 7, 8}
print(a.difference(b))#{1, 2, 3}

#Built in Methods

a={1,2,3,4}
b={2,3}
print(a.issubset(b))#False
print(b.issubset(a))#True
print(girls.isdisjoint(guys))#True
print(guys.isdisjoint(online))#False

print(girls)#{'fareen', 'priya', 'bindu', 'rama', 'varsha', 'preethi', 'ruchitha'}
girls.add('sahithi')
print(girls)#{'priya', 'ruchitha', 'fareen', 'rama', 'sahithi', 'varsha', 'preethi', 'bindu'}
girls.add('meggi')
print(girls)#{'priya', 'rama', 'meggi', 'varsha', 'sahithi', 'preethi', 'ruchitha', 'fareen', 'bindu'}
girls.remove('fareen')
print(girls)#{'priya', 'rama', 'meggi', 'varsha', 'sahithi', 'preethi', 'ruchitha', 'bindu'}
girls.remove('ruchitha')
print(girls)#{'priya', 'rama', 'meggi', 'varsha', 'sahithi', 'preethi', 'bindu'}
girls.discard('ruchitha')
print(girls)#{'priya', 'rama', 'meggi', 'varsha', 'sahithi', 'preethi', 'bindu'}
girls.pop()
print(girls)#{'rama', 'meggi', 'varsha', 'sahithi', 'preethi', 'bindu'}
print(online)#{'pawan', 'kalyan'}
online.clear()
print(online)#set()
print(guys)#{'fazil', 'ahil', 'hussain', 'ahaan', 'kalyan', 'abbu', 'amaan', 'mahaboob'}
guys.update({'shive','vasu','sathish'})
print(guys)#{'ahil', 'vasu', 'ahaan', 'kalyan', 'abbu', 'fazil', 'shive', 'sathish', 'hussain', 'amaan', 'mahaboob'}


c={1,2,3,4,7,8,9}
print(max(c))#9
min(c)
print(min(c))#1
sum(c)
print(sum(c))#34
sorted(c)
s=[1,2,3,4]
print(set(s))#{1, 2, 3, 4}


