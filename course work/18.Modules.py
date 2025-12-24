#.Modules(A group of functions)

#.User define Modules
#.Build in modules

#.Date and time

import datetime
today= datetime.date.today()
print(today)

#.2
from datetime import date
today= date.today()
print(today)

#.3
from datetime import date
today= date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)


#.4

from datetime import date
today= date.today()
print(today.weekday())
print(today.isoweekday())

#.5 Verify module
print(date(2025,12,12))
print(date(2025,11,15))

#.6 Time
from datetime import time,date
print(date(2025,12,12))
print(time(23,16,40))

#.7 date and time
from datetime import time,date,datetime
now= datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.second)

#.8 Format
from datetime import time,date,datetime
now= datetime.now()

print(now.strftime('%y/%m/%d'))
print(now.strftime('%d/%m/%y'))

print(now.strftime('%y/%m/%d %H:%S'))
print(now.strftime('%d/%m/%y %I:%M %S %p'))
print(now.strftime('%A /%d/%m/%y %I:%M %S %p'))
print(now.strftime('%a /%d/%m/%y %I:%M %S %p'))
print(now.strftime('%a, %d %B %y %I:%M %S %p'))
print(now.strftime('%a, %d %b %y %I:%M %S %p'))

#.9 Timedelta
from datetime import time,date,datetime,timedelta
today= date.today()
now= datetime.now()

after7= today+ timedelta(days=7)
after7m= now+ timedelta(minutes=7)
after7h= now+ timedelta(hours=7)
print(after7,after7m,after7h)

#.10

import platform
print(platform.system())
print(platform.release())
print(platform.processor())


#.11

import sys
print(sys.argv)
print("starting")
sys.exit()#terminate the program
print("Ending")



#.12
import random
print(random.random())
print(random.randint(1,10))
print(random.uniform(1,10))

names=['fareen','rama','priya','krishna','sathish','ajay']
print(random.choice(names))
print(random.choices(names,k=3))
print("Before:",names)
random.shuffle(names)
print("After:",names)
   

#.13

import math
print(math.pi)
print(math.e)

print(math.sqrt(16))
print(math.pow(2,5))

print(math.ceil(12.3))
print(math.ceil(12.23))
print(math.ceil(12.00001))
print(math.ceil(12.8))

print(math.floor(12.3))
print(math.floor(12.83))
print(math.floor(12.9999))
print(math.floor(12.9))

print(math.fabs(-12.3))
print(math.factorial(7))

print(math.gcd(50,100))

print(math.sin(30))
print(math.cos(30))
print(math.tan(30))

print(math.log(2,2))

print(math.degrees(30))
print(math.radians(12))

#.14 counter,defaultdict,deque

from collections import Counter,defaultdict,deque
s='python'
s1="Ajay is very late to calss s0 i am giving absent to him"
l=[1,2,3,4,2,1,3,4,5,12,23]
t=(1,2,3,4,2,1,3,4,5,12,23)
se=[1,2,3,4,2,1,3,4,5,12,23]
print(Counter(s))
print(Counter(s1.split()))
print(Counter(l))
print(Counter(t))
print(Counter(se))
#.defaultdict
d=defaultdict(int)
s='python programming'
for i in s:
    d[i]+=1
print(d)
#deque
d=deque([])

d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.popleft()
d.popleft()
d.append(80)
d.append(90)
print(d)

q=deque([])
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
q.appendleft(40)
q.pop()
q.pop()
q.appendleft(80)
q.appendleft(90)
print(q)


#.15 permutations,combinations

from itertools import combinations,permutations
s='abc'
print(list(combinations(s,2)))
print(list(permutations(s,2)))
