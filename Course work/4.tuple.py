'''
Tuple
-------------------------
'''
t=()
t=tuple()
print(t)#()

t=(1,2,3,4,5,1,2,4)
print(t)#(1, 2, 3, 4, 5, 1, 2, 4)
t=tuple((1,2,3,4,5))
print(t)#(1, 2, 3, 4, 5)

t=1,2,3,4,5
print(t)#(1, 2, 3, 4, 5)
t=(1)
print(t)#1
t=[1]
print(t)#[1]
t=(1)
t=(1,)
print(t)#(1,)


t=('int','float','complex','bool','set','dict','list','tuple','string')
print(t[1])#float
print(t[-1])#string
print(t[-2])#tuple
print(t[-5])#set
print(t[2])#complex
print(t[3])#bool


t
('int', 'float', 'complex', 'bool', 'set', 'dict', 'list', 'tuple', 'string')
print(t[3:6])#('bool', 'set', 'dict')
print(t[-1:-4:-1])#('string', 'tuple', 'list')
print(t[-3:]) #('list', 'tuple', 'string')
print(t[2::-1]) #('complex', 'float', 'int')
print(t[::2]) #('int', 'complex', 'set', 'list', 'string')
print(t[::-2]) #('string', 'list', 'set', 'complex', 'int')

t1=(1,2,3)
t2=(7,8,9)
print(t1+t2)#(1, 2, 3, 7, 8, 9)
print(t1*5)#(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
print(t1) #(1, 2, 3)
print(3 in t1)#True
print(5 in t1)#False
print(4 not in t1)#True
print(1 not in t1)#False

t=(10,20,30)
a,b,c=t
print(a)#10
print(b)#20
print(c)#30

t=('Uname','mail@gmail.com','Pwd@123')
print(t[0])#Uname
print(t[1])#mail@gmail.com
print(t[2])#Pwd@123

uname,mail,pwd=t
print(uname)#Uname
print(mail)#mail@gmail.com
print(pwd) #Pwd@123
print(t)#('Uname', 'mail@gmail.com', 'Pwd@123')


t=(1, 2, 3, 1, 2, 3, 1, 2)
print(t.count(2))#3
print(t.count(3))#2
print(t.count(1))#3
print(t.index(2))#1
print(len(t))#8
print(max(t))#3
print(min(t))#1
print(sum(t))#15
print(t)#(1, 2, 3, 1, 2, 3, 1, 2)

