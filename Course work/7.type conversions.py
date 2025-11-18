#Type conversion

#Numeric values only converted into numeric types not collections, and collections converted into only colections not numeric type

a=10
print(float(a))#10.0
print(str(a))#10
print(complex(a))#(10+0j)
print(bool(a))#True
#int cant be converted into list, set, tuple , dictionary  because they are collections , int is a single varible cant iterable

b=12.5
print(int(b))#12
print(str(b))#12.5
print(complex(b))#(12.5+0j)
print(bool(b))#True

#float cant be converted into list, set, tuple , dictionary  because they are collections , int is a single varible cant be iterable
s='Python'
print(list(s))#['P', 'y', 't', 'h', 'o', 'n']
print(tuple(s))#('P', 'y', 't', 'h', 'o', 'n')
print(set(s))#{'P', 'h', 'o', 't', 'n', 'y'}
print(bool(s))#True

#list can be converted into string,tuple,set,bool because they are collections, int,float,complex single variable can't be iterable
l=[1,2,3,4,5]
print(str(l))#[1, 2, 3, 4, 5]
print(tuple(l))#(1, 2, 3, 4, 5)
print(set(l))#{1, 2, 3, 4, 5}
print(bool(l))#True

#tuple can be converted into string,list,set,bool because they are collectinns int,float,complex single variable can't be iterable

t=(1,2,3,4,5)
print(str(t))#(1, 2, 3, 4, 5)
print(list(t))#[1, 2, 3, 4, 5]
print(set(t))#{1, 2, 3, 4, 5}
print(bool(t))#True


#string can be converted into tuple,list,set,bool because they are collectinns int,float,complex single variable can't be iterable

S={1,2,3,4,5}
print(str(S))#{1, 2, 3, 4, 5}
print(list(S))#[1, 2, 3, 4, 5]
print(tuple(S))#(1, 2, 3, 4, 5)
print(set(S))#{1, 2, 3, 4, 5}
print(bool(s))#true

#dictionary can be converted into tuple,list,set,bool because they are collectinns int,float,complex single variable can't be iterable

d=[(1,2),(3,4),(5,6),(7,8)]
print(dict(d))#{1: 2, 3: 4, 5: 6, 7: 8}
d={1:1,2:4,3:9}
print(list(d))#[1, 2, 3]
print(tuple(d))#(1, 2, 3)
print(set(d))#{1, 2, 3}





