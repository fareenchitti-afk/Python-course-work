

data={

    'App ID': 222,
    'App name': 'Hotstar',
    'Version': '24.4.5',
    'Price': 149.00,
    'Discount': 10.00,
    'Catagories': ['Entertainment','OTT','Streaming','Sports'],
    'Downloads and Users': (500000000, 32000000),
    'Features': ('Movies','Series','Live Sports','Kids Content'),
    'Developer_details': {
        'Developer_name': 'Disney+ Hotstar',
        'Contact': 'help@hotstar.com',
        'location':'Mumbai, India'
    }
}

print("\nSample data: \n")

for key, value in data.items():
    if key=='Developer_details':
        for key1, value1 in data['Developer_details'].items():
            print('{}: {}'.format(key1,value1))
    print('{}: {}'.format(key, value))

#Inputs
print('\n'*2)

id = int(input("Enter the App ID:  "))
name=input("Enter Name of the App: ")
version=input("Enter the version of App: ")
price=float(input("Enter the cost of App Subscription: "))
discount=float(input("Enter discount percent for subscription: "))
cat=list(map(str.strip,input("Enter the App categories(comma-separated): ").split(',')))
users=tuple(map(str,input("Enter Downloads and Users: ").split()))
features=set(map(str.strip,input("Enter the features(comma-separated): ").split(',')))
developer_details={
    'developer_name': input("Enter developer name: "),
    'contact': input('Enter developer contact : '),
    'location': input('Enter developer location: ')
}

#Output
print('\n'*3)

#Comma separation
print("App ID: ",id,"\nName: ",name,"\nPrice of Subscription: ",price)

#Percentage Formatting
print("Discount for subscription: %.2f"%(discount))

print("App Version: %s"%(version))

#f-string
print(f"Categories: {', '.join(cat)}")

print(f'Users: {users[0]}')
print(f'Downloads: {users[1]}')

#.format() method
print("Features: {}".format(', '.join(features)))

for key, value in developer_details.items():
    print("{}: {}".format(key,value))


