
from itertools import combinations,combinations_with_replacement

list1=[1,2,3]
result = combinations(list1,3)
"""
start with 1 remaining 2,3 -> 1,2,3 (we cannot do 3,2 since right to left not allowed in combination)
start with 2 remaining 3 -> 2,3 (do nothing since l=3)
start with 3 remaining [] -> (do nothing since l=3)
Final output: 1,2,3
"""
print(list(result)) #OP : [(1, 2, 3)]

# Combinations with length of 2
list1=[1,2,3]
result = combinations(list1,2)
"""
start with 1 remaining 2 -> 1,2
start with 1 remaining 3 -> 1,3
start with 2 remaining 3 -> 2,3
start with 3 remaining [] -> do nothing
final output : (1,2) (1,3) (2,3)
"""
print(list(result)) #OP : [(1, 2), (1, 3), (2, 3)]

list1=[1,2,3]
#Combination with replacement and length of 2
# in combination with replacement same number is allowed!
result = combinations_with_replacement(list1,2)
"""
addition bcoz of replacement -> 1,1
start with 1 remaining 2 -> 1,2
start with 1 remaining 3 -> 1,3
addition bcoz of replacement -> 2,2
start with 2 remaining 3 -> 2,3
addition bcoz of replacement -> 3,3
start with 3 remaining [] -> do nothing
final output :(1,1) (1,2) (1,3) (2,2) (2,3) (3,3)
"""
print(list(result)) #OP : [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]