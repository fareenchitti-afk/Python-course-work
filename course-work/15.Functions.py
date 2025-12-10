#.Function(Function is a block of code)

#.1
def func_name():
    #stmts
    print("This a function")
    
func_name()
func_name()
func_name()
func_name()

def wish(name):
    print(f'Welcome to codegnan {name}')

wish('abc')
wish('def')
wish('rty')



#.2

def display(username,maim,pwd):
    print(f'Username: {username}\nMail:{mail}\nPassword:{pwd}')

uname=input("Enter the username: ")
mail=input("Enter the mail: ")
pwd=input("Enter the Password: ")

display(uname,mail,pwd)
display(mail,uname,pwd)
display(pwd,uname,mail)
display(uname,pwd,mail)


#.3

def display(username,mail,pwd):
    print(f'Username: {username}\nMail:{mail}\nPassword:{pwd}')

uname=input("Enter the username: ")
mail=input("Enter the mail: ")
pwd=input("Enter the Password: ")

display(username=uname,mail=mail,pwd=pwd)
display(pwd=pwd,username=uname,mail=mail)
display(username=uname,pwd=pwd,mail=mail)

#.4
def display(*names):
    print(names)

names=input("Enter the names: ").split()
display('fareen','farhana','fazil','haseena','mahaboob')
display('ahaan','ahil','ayesha','sameera')
display('hussain','saheb','reshma')
display('ashu','ani')
display('afreen')

#.5
def squares(**numbers):
    print(numbers)

squares(k1='1',k2='2',k3='3')
squares(k1='1',k2='2')
squares(k1='1',k2='2',k3='3',k4='4')
squares(k1='1',k2='2',k3='3',k4='4',k5='5')

#.6
name='fareen'
def data():
    print("Inside:",name)

print("Outside:",name)
data()

#.or
name='fareen'
def data(name):
    name='fareen'
    print("Inside:",name)
    
data(name)
print("Outside:",name)


#.7

def status():
    course='Java'
    print("Beg:",course)
    def change():
        nonlocal course
        course='python'
        print("In Btw:",course)

    change()
    print("Final:",course)

status()
