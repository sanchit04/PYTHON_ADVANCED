# SETS are unordered, mutable and no duplicates
set1={1,2,3,4,4,4}
print(set1) #OP -> {1, 2, 3, 4} (Removed the duplicates)

# using set function
set1=set("hello")
print(set1) #OP -> {'o', 'h', 'e', 'l'}
# can be used to find how many characters are present in your string
# TODO form a lambda function to count number of characters in the list or set.
list1=['o', 'h', 'e', 'l']
freq=lambda lst: {ch: lst.count(ch) for ch in set(list1)}
print(freq(list1))

# Above lambda function takes input as list
# and then returns a dictionary ch -> key and value is count of ch
#OP :{'e': 1, 'o': 1, 'h': 1, 'l': 1}

set2=set([4,4,2,5,1])
print(set2)

# CREATING AN EMPTY SET
set1={}
print(type(set1)) #OP THIS IS NOT CORRECT WAY OF CREATING EMPTY SET THIS WILL CREATE A EMPTY DICT
 # <class 'dict'>

# Correct way of creating empty set:
set1=set()
print(type(set1))
print(set1)
#OP:
# <class 'set'>
# set()

# Adding elements to set works since set are mutables
# using add method:
# Can add any datatype element
set1.add(4)
set1.add("hello")
print(set1) # OP -> {'hello', 4}

# Removing element from set
#using remove method
set1.remove("hello")
print(set1) #OP -> {4}

# removing non existing element from set
#set1.remove("grapes")
#print(set1)
#OP -> Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/sets.py", line 46, in <module>
#     set1.remove("grapes")
# KeyError: 'grapes'

#using discard method
set1.add("Sanchit")
set1.discard("Sharvari") # IF element is not present it wont throw any key error like remove method
print(set1) #OP -> {4, 'Sanchit'}

# Empty entire set
set1.clear()
print(set1) #OP -> set()

# Using POP method in set
set1.add("Sanchit")
set1.add("Sharvari")
print(set1) #OP {'Sanchit', 'Sharvari'}
print(set1.pop()) #OP Removes any random element from the set -> Sanchit

#POP on an empty set
# set1.clear()
# print(set1.pop()) #OP: KeyError: 'pop from an empty set'

# ITERATING ON A SET
print(set1)
for i in set1:
    print(i)
#OP :
# {'Sharvari'}
# Sharvari

# Check existence of element in a set
set1={"Sanchit","Sharvari"}
if 'Sharvari' in set1:
    print("Its present")






