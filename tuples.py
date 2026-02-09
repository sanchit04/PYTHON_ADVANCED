# Tuples are ordered immutable (cannot be modified after instantiation) allows duplicate elements
# it can have any data type elements
# Tuples are created using , (paranthesis) is optional

tuple1="Alex","Gawde",29 # Paranthesis are optional
print(type(tuple1)) #O/P -> <class 'tuple'>

#Creating tuple with single element:
tuple1=("Alex")
print(type(tuple1)) # O/P <class 'str'> (Not correct way of creating tuple,
# tuple needs to be created with atleast 1 comma)

tuple1=("Alex",)
print(type(tuple1)) #OP -> <class 'tuple'>

# Creating tuple from tuple function
tuple1 = tuple([1,2,3,4]) # tuple function takes iterable as a input argument
# , list, sets, string are iterable which are allowed, dict is also allowed but
# only keys with the respective datatype will be stored as elements
print(tuple1) #OP -> (1, 2, 3, 4)

tuple1 = tuple("HelloWorld")
print(tuple1) #OP -> ('H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd')

# When we pass
tuple1 =tuple ({1:"hello"})
print(tuple1[0]) #OP -> 1
print(type(tuple1[0])) #OP -> <class 'int'>

tuple1=tuple(dict(name="Alex",age=35))
print(tuple1) # ('name', 'age') -> keys of dicts are stored
print(type(tuple1[0])) #OP -> <class 'str'>
