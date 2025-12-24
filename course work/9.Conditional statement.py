#.Conditional statement

'''
simple if
if- else
if- elif.......-else
nested if if- else -else     
'''

#.simple if
send=True
if send:
    print("send the message")

send=False
if send:
    print("send the message")

followers=[]
click=True
if click:
    followers.append("userl")

#.if else
data={'fareen@gmail.com':1234, 
      'farhana@gmail.com':4563,
      'fazil@gmail.com':2222,
      'ahil@gmail.com':1267
      }
mail=input("Enter the mail: ")
pwd=int(input("Enter the passward: "))

if data.get(mail)==pwd:
     print("valid Login")
else:
    print("Invalid Login")

#if- elif.........-else
amount=int(input("Enter the amount"))
actual_amount=amount
if amount>10000:
    actual_amount=amount- amount*0.5
elif 8000<amount<=10000:
    actual_amount=amount- amount*0.3
elif 5000<amount<=8000:
    actual_amount=amount- amount*0.2
elif 2000<amount<=5000:
    actual_amount=amount- amount*0.05

print(f"Amount:{amount}\nAfter discount:{actual_amount}")

budget=int(input("Enter the budget:"))
if budget > 20000:
    print("Trip to kerala")

elif 15000 <= budget < 20000:
    print("Go for shopping")

elif 10000 <= budget < 15000:
    print("Clubbing")

elif 5000 <= budget < 10000:
       print("Go for Cafe")

elif 2000 <= budget < 5000:
     print("Go for Movie")
elif 1000 <= budget < 2000 :  
     print("Go for lunch")
elif 500 <= budget < 1000 : 
     print("Go for nail art")
else:
    print("Go to sleep")


data={
    1:'Rama will Sing',
    2:'Telugu dialogue - priya',
    3:'Fareen will give party',
    4:'Ask guestion - Farhan',
    5:'Ramp Walik - Ahil',
    6:'Anthing - Ahaan'
}

print(data)

ch=int(input("Enter the choice:"))
if 1<=ch<=6:
    print(data[ch])

else:
    print("Invalid choice")

#.nested if else

products=['laptop','mouse','phone','keyboard', 'charger', 'speaker']
stocks=[100,20,500,0,200,6]


print("*"*30)
print(products)
print("*"*30)
network=True

if network:
    product=input("Enter the products:").strip()
    if product in products:
        index = products.index(product)
        if stocks[index]==0:
            print(f'{product}- out of stock')
        elif 1<=stocks[index]<=10:
             print(f'{product}- Out few items left. Hurry Up')
        else:
            print(f'{product}')
    else:
        print("product not found")
else:
    print("Check out the network")

data={
    'fareen':{'python':99,'mysql':88,'flask':90},
    'farhana':{'python':29,'mysql':100,'flask':50},
    'fazil':{'python':98,'mysql':96,'flask':99},
    'ahil':{'python':85,'mysql':86,'flask':89},
    'ahaan':{'python':50,'mysql':70,'flask':60},
    'ahaan':{'python':10,'mysql':20,'flask':30},
}
user=input("Enter the user")
avg=(data[user]['python']+data[user]['mysql']+data[user]['flask'])
if 80<=avg<=100:
     print(f'{user} got "A" grade. \nkeep it up')
elif 60<=avg<=80:
    print(f'{user} got "B" grade. \ngood , need to improve')
elif 40<=avg<=60:
     print(f'{user} got "C" grade. \navg , practice well')
elif avg<40:
     print(f'{user} got"F" grade. \nfail, bring your parents')

    
    