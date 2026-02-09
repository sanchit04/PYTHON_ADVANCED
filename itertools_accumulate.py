#Accumulate will compute between each element in the list

from itertools import accumulate
import operator

list1=[1,2,3,4]
result = accumulate(list1)
"""
By default accumulate will be sum
1
1+2 -> 3
3+3 -> 6
6+4 -> 10

final: [1,3,6,10]
"""
print(list(result)) #OP [1, 3, 6, 10]

# TO DO MULTIPLICATION USING ACCUMULATE
list1=[1,2,3,4]

# we are setting func as operator.mul which is multiplication operation
result = accumulate(list1,func=operator.mul)
"""
By default accumulate will be sum
1
1*2 -> 2
2*3 -> 6
6*4 -> 24

final: [1,2,6,24]
"""
print(list(result)) #OP [1, 2, 6, 24]

# MAX FUNCTION USING ACCUMULATE
list1=[1,2,3,5,6,8,2,1]
result = accumulate(list1,func=max)
"""
1
2 is greater than 1 -> 2
3 is greater than 2 -> 3
5 is greater than 3 -> 5
6 is greater than 5 -> 6
8 is greater than 6 -> 8
8 is greater than 2 -> 8 (IMPORTANT)
8 is greater than 1 -> 8 (IMPORTANT)
"""
print(list(result)) #OP [1, 2, 3, 5, 6, 8, 8, 8]
