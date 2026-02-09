from itertools import permutations

list1=[1,2,3]
result = permutations(list1)
"""
start with 1 remaining -> 2,3 -> possible combinations 2,3 and 3,2 -> (1,2,3) (1,3,2)
start with 2 remaining -> 1,3 -> possible combinations 1,3 and 3,1 -> (2,1,3) (2,3,1)
start with 3 remaining -> 1,2 -> possible combinations 1,2 and 2,1 -> (3,1,2) (3,2,1)
"""
print(list(result)) #OP : [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# PERMUTATION WITH LENGTH OF 2:
result = permutations(list1,2)
"""
Start with 1 remaining -> 2 -> 1,2
Start with 1 remaining -> 3 -> 1,3
Start with 2 remaining -> 1 -> 2,1
Start with 2 remaining -> 3 -> 2,3
Start with 3 remaining -> 1 -> 3,1
Start with 3 remaining -> 2 -> 3,2
"""
print(list(result)) #OP: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
