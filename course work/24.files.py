#.Read mode

try:
    file= open('class.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    file.close()

#.Read line

try:
    file= open('class.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.readline())
    file.close()

#.Read lines

try:
    file= open('class.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.readlines())
    file.close()


try:
    file= open('class.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    print(file.readline())
    print(file.readlines())
    file.close()

#.Seek

try:
    file= open('class.txt','r')
except FileNotFoundError:
    print("File is not present")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    file.close()

#.or
try:
    with open('class.txt','r') as file:
        print(file.read())
        file.seek(0)
        print(file.readline())
        file.seek(0)
        print(file.readlines())

except FileNotFoundError:
    print("File is not present")
        


#.write mode

with open('class.txt','w') as file:
     file.write("File operations")

#.Append mode

with open('classes.txt','a') as file:
    file.write("Exception handling")

#.read and append at same time

with open('classes.txt','a+') as file:
    file.write("\nException handling............")
    file.seek(0)
    print(file.read())
    

#.right method
with open('classes.txt','r+') as file:
    file.write("\nException handling............")
    file.seek(0)
    print(file.read())
    

#.Creating empty folder
import os
os.mkdir("pfs-41")

#.Removing empty folder
import os
os.rmdir("pfs-41")

import os
import shutil
os.rmdir('pfs-41')
