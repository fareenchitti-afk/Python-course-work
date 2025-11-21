#.Control Statements
'''
for var in seq:
    #stmts
for var in enumerate(seq):
    #stmts
for var in range (start,end+1,step):
    #stmts
for i in range(len(seq)):
    # #stmts
seq: list,tuple,set,dict,str,range()
'''
#.list

lang=['python','java','c','c++','mysql','ds','flask','javascript']
for i in lang:
    print(i)
for i in enumerate(lang):
    print(i)
    print(i,i[0],i[1])
    
#.list and tuple are same and i in lang: is  correct method to literate word 

#.set

lang={'python','java','c','c++','mysql','ds','flask','javascript'}
for i in lang:
    print(i)

#.dict
    
lang={1:'python',2:'java',3:'c',4:'c++'}
for i in lang:
    print(f'key-{i} value-{lang[i]}')

for i in enumerate(lang):
    
      print(f'index-{i[0]} key-{i[1]} value-{lang[i[1]]}')

#.string
lang='python programming'
for i in lang:
    print(f'{i}')
for i in enumerate(lang):
    
    print(f'index-{i[0]} val-{i[1]}')

#.range()

for i in range(1,11):
    print(i)
    for i in range(1,101,2):
        print(i)
num=int(input("Enter the number:"))
for i in range (1,21):
    print(f'{num}*{i}={num*i}')
for i in range (20,0,-1):
    print(i)
    for i in range (3,100,3):
        print(i)

l=['laptop','mouse','charger','keyboard']
for i in range (len(l)):
    print(i,l[i])

    
