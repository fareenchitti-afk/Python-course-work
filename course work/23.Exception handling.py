#.Exceptional handling have four type
#.try,Except,finnaly,else

#.single exception handling

try:
    a=10/0

except ZeroDivisionError:
    print("You can't divide a number with zero")

#.Multiple Exception handling
try:
    a=10/0

except ZeroDivisionError:
    print("You can't divide a number with zero")

try:
    a=b/10
except NameError:
    print("You din't define the variable")

try:
    a=int([1,2,3])
except TypeError:
    print("you can change this datatype into another one")

#.Muliple errors at one time

try:
    a=int([1,2,3])

except (ZeroDivisionError,NameError,TypeError,KeyError,IndexError)as e:
    print("Error Occured:",e)

    #.or

try:
    a=a+[1,2,3]

except Exception as e:
    print("Error Occured:",e)
   

else:    
    print("You have divided successfully")

finally:
    print("end of the try block")

print("rest of the code")

#.Raise error

try:
    a=int(input("Enter the number: "))
    if a<0:
        raise Exception("Negitive number not allowed")
except Exception as e:
    print("Error Occured:",e)

#.Nested try block

try:
    a=int(input("Enter the number: "))
    try:
        a=b/10
    except Exception as e:
        print("Error Occured:",e)

except Exception as e:
    print("Error Occured:",e)
    
    
