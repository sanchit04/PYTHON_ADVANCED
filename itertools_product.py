from itertools import product

a=[1,2]
b=[3,4]

result = product(a,b)
print(result) # <itertools.product object at 0x1021a7780>
print(list(result)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

#PRODUCT with repeation of 2
#single list

a =[1,2]
result = product(a,repeat=2)
"""
since repeat of 2
box1: [1,2]
box2: [1,2]

(1,1)(1,2)(2,1)(2,2)
"""
print(list(result)) # [(1, 1), (1, 2), (2, 1), (2, 2)]

# two lists
a=[1,2]
b=[3,4]

"""
since repeat 2
box1: [1,2]
box2: [3,4]
box3: [1,2]
box4: [3,4]

(1,3,1,3)(1,3,1,4)(1,3,2,3)(1,3,2,4)(1,4,1,3)(1,4,1,4)(1,4,2,3)(1,4,2,4)(2,3,1,3)(2,3,1,4)(2,3,2,3)(2,3,2,4)(2,4,1,3)(2,4,1,4)(2,4,2,3)(2,4,2,4)
"""
result = product(a,b,repeat=2)
print(list(result))

a=[1,2]
b=[3]

"""
repeat 2
box1: [1,2]
box2: [3]
box3: [1,2]
box4: [3]

(1,3,1,3)(1,3,2,3)(2,3,1,3)(2,3,2,3)
"""

result = product(a,b,repeat=2)
print(list(result))