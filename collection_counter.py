# COUNTER, namedTuple, OrderedDict, DefaultDICT, deque

from collections import Counter

temp_string = "aaaaaabbbbbcccdddeefff"
# Counts the numer of occurrence each character has and returns a dict of it
my_counter = Counter(temp_string)
print(my_counter) #OP -> Counter({'a': 6, 'b': 5, 'c': 3, 'd': 3, 'f': 3, 'e': 2})
# To print the dict key values using items()
for key,value in my_counter.items():
    print(key,value)

print(my_counter.keys()) #OP -> dict_keys(['a', 'b', 'c', 'd', 'e', 'f'])
print(my_counter.values()) #OP -> dict_values([6, 5, 3, 3, 2, 3])

# TO FIND MOST REPETITIVE ELEMENT using counter and most_common
# Accessing first element of list, then accessing first element of tuple
# this one finds one most_common element
print(my_counter.most_common(1)[0][0]) # OP ->[('a', 6)] -> [0][0] -> a

# if we need to find two most_common element
print(my_counter.most_common(2)) # OP -> [('a', 6), ('b', 5)]

# if we dont give anything in most_common() argument then it will give all
print(my_counter.most_common()) #OP -> [('a', 6), ('b', 5), ('c', 3), ('d', 3), ('f', 3), ('e', 2)]

#Using Counter to convert string to list:
# .elements gives an iterable object
list1 = list(my_counter.elements())
print(list1)
