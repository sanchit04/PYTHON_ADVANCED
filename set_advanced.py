# UNION AND INTERSECTION IN SETs

odds = {1,3,5,7,9}
evens = {10,0,2,4,6,8}
primes = {10,2,3,5,7}

#IMPORTANT : union, intersection and difference
# will always create a new set it does not modifies the existing set!

u=odds.union(evens)
# UNION Creates a new set
# Combines both removes duplicates and orders them
print(u)# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#Intersection
i=evens.intersection(primes)
# Intersection create a set with only common elements from both
# Orders them
print(i) # {2,10}

# Difference b/w two sets
set_A = {1,2,3,4,5,6,7,8,9}
set_B = {1,2,3,10,11,12}

# returns all the element from setA that are not present in setB
diff = set_A.difference(set_B)
print(diff) #OP -> {4,5,6,7,8,9}

# symmetric_difference
# returns all the elements from setA and setB which are not present in both

diff = set_A.symmetric_difference(set_B)
print(diff) #OP -> {4,5,6,7,8,9,10,11,12}

# UPDATE IN SETS:
set_A = {1,2,3,4,5,6,7,8,9}
set_B = {1,2,3,10,11,12}
# modifies the existing set in this case set_A is LHS and LHS of update will always be updated
# Thus set_A is updated
# Combines all the elements removes duplicates adds from set_B the ones which are missing in set_A
print(set_A.update(set_B)) # OP -> PRINT OF update will be None
print(set_A) # OP -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# INTERSECTION_UPDATE in SETS:
set_A = {1,2,3,4,5,6,7,8,9}
set_B = {1,2,3,10,11,12}
# Only keeps the same elements from both sets in setA all the elements from setA are removed
set_A.intersection_update(set_B)
print(set_A)

# DIFFERENCE_UPDATE in SETS:
set_A = {1,2,3,4,5,6,7,8,9}
set_B = {1,2,3,10,11,12}
# Only keeps the elements from setA which are not present in SET B common ones are also discarded
set_A.difference_update(set_B)
print(set_A) # {4, 5, 6, 7, 8, 9}

# SYMMETRIC_DIFFERENCE_UPDATE IN SETS:
set_A = {1,2,3,4,5,6,7,8,9}
set_B = {1,2,3,10,11,12}
# Only keeps elements from setA and setB which are not present in both, commons are discarded
set_A.symmetric_difference_update(set_B)
print(set_A) #OP {4, 5, 6, 7, 8, 9, 10, 11, 12}

#SUBSETS in SETS

set_A = {1,2,3,4,5,6,7,8,9}
set_B = {1,2,3}
#  all elements of first set (setA) should be present in second set (setB)
# Returns a Boolean value
#SUBSET:
print(set_A.issubset(set_B)) #OP -> False
print(set_B.issubset(set_A)) #OP -> True

# SUPERSET in SETS
# If first set contains all elements of second set then first is the superset of second
print(set_A.issuperset(set_B)) #OP -> True
print(set_B.issuperset(set_A)) #OP -> False

# DISJOINT IN SETS
# There should be no element that is present in both sets then it will be True
print(set_A.isdisjoint(set_B)) #Op -> False

# COPYING SETS (Follows same logic as list assignment operator will just create reference but not new set)
# To create a new set:

set_B = {1,2,3}
set_copy = set(set_B)
print(set_copy)

#Other way
set_copy = set_B.copy()
print(set_copy)

# FROZEN SET -> Creates Immutable version of set
set_frozen = frozenset(set_B)
#set_frozen.add(4)
#O/P:
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/set_advanced.py", line 93, in <module>
#     set_frozen.add(4)
# AttributeError: 'frozenset' object has no attribute 'add'
#set_frozen.remove(4)
#O/P:
# AttributeError: 'frozenset' object has no attribute 'remove'

set_frozen1 = frozenset([1,2,3,46,56])
set_frozen2 = frozenset([4,6,7,2])

# UPDATES DO NOT WORK FOR FROZENSET:
#set_frozen1.intersection_update(set_frozen2)

# DIFFERENCE, INTERSECTION AND UNION WORKS which creates a new set

set_frozen3=set_frozen1.union(set_frozen2)
print(set_frozen3)




