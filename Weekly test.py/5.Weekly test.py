
#.1

import math
circle_geometry=lambda r: (round(math.pi*r*r,2),round(2*math.pi*r,2))
print(circle_geometry(7))
print(circle_geometry(2.5))

#.2
import random
def pick_random_team(members, team_size):
    print(random.choices(members,k=team_size))
pick_random_team(["alice","BOb","Charlie","David"],2)
pick_random_team(["A","B","c","D","E"],3)

#.3
temp=[36,42,39,45,41]
res=list(filter(lambda x:x>40,temp))
print(res)

#.4

n=int(input("Enter the numbers: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
        break
if c==2:
    print("Prime number")
else:
    print("Not Prime number")


#.or
def is_prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
    
n=int(input("Enter the numbers: "))
print(is_prime(n))

#.5
def reverse_number(n):
    if n<=0:
        return
    print(n%10,end='')
    return reverse_number(n//10)
reverse_number(12398765434)


#.6
inp=["cat","car","bat","apple"]
ch='c'
res= list(filter(lambda i:i.startswith(ch),inp))
print(res)


#.7

#string_utils.py
def is_palindrome(word):
    if word== word[::-1]:
        return True
    else:
        return False

def capitalize_words(text):
    return text.capitalize()


#main.py
#from string_utils import is_palindrome,capitalize_words
print(is_palindrome("madam"))
print(capitalize_words("hello world"))

#.8

words=["Apple","apple","BANANA","Cherry"]
res= set(map(lambda i : i.lower(),words))
print(res)

#.9

def coundown(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())
c=coundown(n)
for i in range(n+1):
    print(next(c))


#.10
    
def nested_sum(n):
    total = 0
    for item in n:
        if type(item) == list:
            total += nested_sum(item)
        else:
            total += item
    return total


print(nested_sum([[1, 2], [3, [4, 5]]]))
