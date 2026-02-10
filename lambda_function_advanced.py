#MAP
# Syntax map(func,seq) seq -> is an iterable object

# Getting squares of each element in a list
list1=[1,2,3,4]
result = map(lambda x: x**2,list1)
print(list(result)) # OP: [1, 4, 9, 16]

#Filter
# syntax filter(func (func should return boolean value for this to work),seq)

# filter values which are less than 3
list1=[1,2,3,4]
result = filter(lambda x:x<3,list1)
print(list(result)) #OP: [1, 2]

#Reduce
# Applies function to each element and returns a single value
# It will always take two input argument
# Does not return a iterable object
# syntax reduce(func,seq)

from functools import reduce
a=[1,2,3,4]
result = reduce(lambda x,y:x*y,a)
"""
1*2 -> 2
2*3 -> 6
6*4 -> 24
"""
print(result) #OP : 24
