# data={

#     'App ID': 111,

#     'App name': 'Netflix',

#     'Version': '8.121.0',

#     'Price': 649.00,

#     'Discount': 5.00,

#     'Catagories': ['Entertainment','Ott','Online','Streaming'],

#     'Downloads and Users': (1000000000, 75000000),

#     'Features': ('Movies','Series','Offline download'),

#     'Developer_details': {

#         'Developer_name': 'Netflix Inc',

#         'Contact': 'help@netflix.com',

#         'location':'California, USA'

#     }

# }



# print("\nSample data: \n")



# for key, value in data.items():

#     if key=='Developer_details':

#         for key1, value1 in data['Developer_details'].items():

#             print('{}: {}'.format(key1,value1))

#     print('{}: {}'.format(key, value))



#Inputs

print('\n'*2)



id = int(input("Enter the App ID:  "))

name=input("Enter Name of the App: ")

version=input("Enter the version of App: ")

price=float(input("Enter the cost of App Subscription: "))

discount=float(input("Enter discount percent for supscription: "))

cat=list(map(str.strip,input("Enter the App categories(comma-seperated): ").split(',')))

users=tuple(map(str,input("Enter Downloads and Users: ").split()))

features=set(map(str.strip,input("Enter the features(Comma-seperated): ").split(',')))

developer_details={

    'developer_name': input("Enter developer name: "),

    'contact': input('Enter developer contact : '),

    'location': input('Enter developer location: ')

}



#Output

print('\n'*3)



#Comma seperation



print("App ID: ",id,"\nName: ",name,"\nPrice of Subscription: ",price)



#Percentage Formatting



print("Discount for subscription: %.2f"%(discount))



print("App Version: %s"%(version))



#f-string



print(f'Catagories: {', '.join(cat)}')



print(f'Users: {users[0]}')



print(f'Downloads: {users[1]}')



#.format() method

print("Features: {}".format(', '.join(features)))



for key, value in developer_details.items():

    print("{}: {}".format(key,value))