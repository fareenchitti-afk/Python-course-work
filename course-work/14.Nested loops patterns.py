#.nested

for row in range(5):
    for col in range(5):
        print(row,end='')
        print()


for row in range(5):
    for col in range(row+1):
        print(row,end='')
    print()


n=int(input("Enter the size:"))

for row in range(n):
    for col in range(n-row):
        print(row,end='')
    print()


n=int(input("Enter the size:"))

for row in range(n):
    for spc in range(n-1-row):
        print('',end='')
    for col in range(row+1):
         print('*',end='')
    print()


n=int(input("Enter the size:"))

for row in range(n):
    for spc in range(row+1):
        print(' ',end=' ')
    for col in range(n-1-row):
         print('*',end=' ')
    print()


n=int(input("Enter the size:"))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1 or row==n//2:
    
         print('*',end=' ')
        else:
           print(' ',end=' ')
    print()


n=int(input("Enter the size:"))

for row in range(n):
    for col in range(n):
        if row==0 or col==0 or row==n-1 or col==n-1: 
    
         print('*',end=' ')
        else:
           print(' ',end=' ')
    print()


n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if j%2:
            print("0",end='')
        else:
            print("1",end='')

    print()
n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if j%2:
            print("0",end='')
        else:
            print("1",end='')
          

n=int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i< j:
            print(0,end='')
        else:
            print(1,end='')

    print()
  
  
