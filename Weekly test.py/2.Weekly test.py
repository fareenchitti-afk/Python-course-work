date=input("Enter the date: ").split('-')
print(f'{date[2]}/{date[1]}/{date[0]}')


n=int(input("Enter the n:"))
if n%2==0:
    print("Even Winner")
else:
    print("Odd Winner")


s=input("Ente the string: ").lower()
s=s.replace('a','*')
s=s.replace('e','*')
s=s.replace('i','*')
s=s.replace('o','*')
s=s.replace('u','*')
print(s)

print(s.translate(str.maketrans('aeiou','*****')))


prices=list(map(float,input("Enter the prices: ").split()))
print(sum(prices))
print(max(prices))


credentials = ("admin", "python123")
username=input("Enter the username: ")
password=input("Enter the password: ")

if (username,password)==credentials:
    print("Login valid")
else:
    print("Invalid Login")



names=input("Enter the names: ").split(',')
print(sorted(set(names)))


data={}
n=int(input("Enter the n: "))
for i in range(n):
    name,mark= input().split()
    data[name]=int(mark)


name=None
max_marks=0

for i in data:
    if data[i]>max_marks:
        name=i
        max_marks=data[i]


print(name)


sen=input("Enter the sentence").split()
s=''
for i in sen:
    s+=i[::-1]+' '

print(s)


nums=list(map(int,input().split()))

while 0 in nums:
    nums.remove(0)

print(nums)

res=[]
for i in nums:
    if i!=0:
        res.append(i)
        
print(res)


sen=input()
res={}
for i in sen:
    if i!=' ':
        res[i]=sen.count(i)

print(res)