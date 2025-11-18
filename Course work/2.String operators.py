#.Operations on stringss=''
'''s=""
s=''' '''
s="' '" '''
#1.Concatenation
name='Fareen'
name1="Hassena"
name2=name+ name1
print(name2)#FareenHassena

#2.Repetition
name+' '+name1
print(name+'  '+name1)#Fareen  Hassena

#3.Indexing
name * 10
print(name * 10)#FareenFareenFareenFareenFareenFareenFareenFareenFareenFareen
name='FareenHaseena'
print(name[3])#e
print(name[-2])#n
print(name[-5])#s
print(name[1])#a

#4.Slicing
names='FareenHaseenaMahaboobFarhanaFazilhussain'
print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names[0:4])#Fare
print(names[:4])#Fare
print(names[4:11])#enHasee
print(names[11:17])#naMaha
print(names[17:25])#boobFarh
print(names[25:32])#anaFazi
print(names[32:40])#lhussain
print(names[32:])#lhussain
print(names[0:4:2])#Fr
print(names[::3])#FeHeahoFhazhsn
print(names[-8:])#lhussain


#5.Membership
print(names[-15:-8])#anaFazi
print(names[-23:-15])#boobFarh
print(names[-29:-23])#naMaha
print(names[-36:-29])#enHasee
print(names[-40:-36])#Fare
print(names[::-1])#niassuhlizaFanahraFboobahaManeesaHneeraF

#1. Case Conversion Methods


print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names[4::-1])#eeraF
print(names[3::-1])#eraF
print(names[10:4])#eesaHn
print(names[10:4:-1])#eesaHne
print(names[10:3:-1])#ahaMan
print(names[16:10:-1])#hraFboob
print(names[24:16:-1])#izaFana
print(names[31:24:-1])#niassuhl
print(names[39:31:-1])#FareenHaseenaMahaboobFarhanaFazilhussain



print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names.upper())#FAREENHASEENAMAHABOOBFARHANAFAZILHUSSAIN
print(names.lower())#fareenhaseenamahaboobfarhanafazilhussain
print(names.swapcase())#fAREENhASEENAmAHABOOBfARHANAfAZILHUSSAIN


l='python programming language'
print(l.capitalize())#Python programming language
print(l.title())  #Python Programming Language
print("ß".casefold())#ss


'python programming language'
print(l.center(100,'*'))#************************************python programming language*************************************
print(l.center(50,'*'))#***********python programming language************
print(l.center(50,'-'))#-----------python programming language------------
print(l.center(50,'_'))#___________python programming language____________
print(l.ljust(50,'-'))#python programming language-----------------------
print(l.ljust(50,' ')+':') # python programming language                       :          
print(l.rjust(50,'-'))#-----------------------python programming language
print('2'.zfill(6))#000002
print( '202'.zfill(6))#000202
print( '202123'.zfill(6))#202123


print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names.find('e'))#3
print( names.find('a'))#1
print( names.find('Fareen'))#0
print( names.find('x'))#-1
print(names.rfind('a'))#37
print( names.index('n'))#5
print(names.index('a'))#1
print(names.rindex('a'))#37


print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names.count('a'))#10
print(names.count('e'))#4
print(names.count('i'))#2


print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names.replace('a','*'))#F*reenH*seen*M*h*boobF*rh*n*F*zilhuss*in
print(names.replace('ee',''))#FarnHasnaMahaboobFarhanaFazilhussain
print(names.replace('ee','00'))#Far00nHas00naMahaboobFarhanaFazilhussain
print(names.replace('ee','-00-'))#Far-00-nHas-00-naMahaboobFarhanaFazilhussain
print(names.replace('Fareen','Shaik'))#ShaikHaseenaMahaboobFarhanaFazilhussain


print(names)#FareenHaseenaMahaboobFarhanaFazilhussain
print(names.maketrans('aeiou','*****'))#{97: 42, 101: 42, 105: 42, 111: 42, 117: 42}
print(names.translate(names.maketrans('aeiou','*****')))#F*r**nH*s**n*M*h*b**bF*rh*n*F*z*lh*ss**n
print(names.translate(names.maketrans('AEIOUaeiou','1234500000')))#F0r00nH0s00n0M0h0b00bF0rh0n0F0z0lh0ss00n
print(names.translate(str.maketrans('AEIOUaeiou','1234500000')))#F0r00nH0s00n0M0h0b00bF0rh0n0F0z0lh0ss00n

#. Splitting & Joining Methods
#1. split(sep)
s='python programming lang'
print(s.split())#['python', 'programming', 'lang']
print(s.split('o'))#['pyth', 'n pr', 'gramming lang']
s='python,java,sql,flask,html,css'
print(s.split(','))#['python', 'java', 'sql', 'flask', 'html', 'css']
      
#2.rsplit(sep)
print(s.rsplit(','))#['python', 'java', 'sql', 'flask', 'html', 'css']
print(s.rsplit(',',3))#['python,java,sql', 'flask', 'html', 'css']
      
#3.splitlines()

s='''python
java
sql
flask
html
css'''
print(s)
print(s.splitlines(','))


#4.Join(iterable)
print(','.join(s))
print(' '.join(s))
print('@'.join(s))
print('\n,'.join(s))

#5.Partition(sep)
s='python,java,sql,flask,html,css'
print(s.partition(','))
print(s.rpartition(','))
#6.rpartiton(sep)
s='python.py'
print(s.rpartition('.'))

