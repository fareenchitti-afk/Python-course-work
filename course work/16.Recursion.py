#.Recursion

def shooting(bullets):
    if bullets<=0:
        print("Game Over")
        return
    print(f'{bullets} bullets left')
    shooting(bullets-1)
    
shooting(10)



def display(n):
    if n>10:
        print("Exit")
        return
    print(n)
    display(n+1)

display(1)


def display(n):
    if n>10:
        print("Exit")
        return
   
    display(n+1)
    print(n)

display(1)



def display(n,i):
    if i>=len(n):
        print("Exit")
        return
    display(n,i+1)
    print(n[i])

display("Codegnan",0)


def display(n,i):
    if i>len(n):
        return
    print(n[:i])
    display(n,i+1)

display("abcdef",1)


def display(n,i):
    if i>len(n):
        return
    print(n[:i])
    display(n,i+1)
    print(n[:i])


def display(n,i):
    if i>len(n):
        return
    print(n*i)
    display(n,i+1)
    
display("abcdef",1)


def display(n,i):
    if i>len(n):
        return
    print(n*i)
    display(n,i+1)
    
display("abcdef",1)

