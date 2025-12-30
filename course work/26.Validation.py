
#.Validation
#.username
import re
name= input("Enter the name: ")
pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res= bool(re.fullmatch(pattern,name))
print(res)

#.email

import re
email= input("Enter the name: ")
pattern = r'^[a-zA-Z0-9,-]+@[a-zA-Z0-9,-]+\.[a-zA-Z]{2,}$'
res= bool(re.fullmatch(pattern,email))
print(res)


#.phone number

import re
phn= input("Enter the phone: ")
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
res= bool(re.fullmatch(pattern,phn))
print(res)


#.Password

import re
pwd= input("Enter the password: ")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res= bool(re.fullmatch(pattern,pwd))
print(res)
