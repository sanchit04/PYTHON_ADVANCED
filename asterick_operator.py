# ASTTERICK OPERATOR:

# Multiplication:
print(5*10) # 50

# Power
print(2**3) # 8

# Create list, tuple, strings with repeated elements
print([0]*10) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print([0,1]*10) # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] (total 20 each 10)

# Similar logic applies to tuples and strings

# *args, **kwargs

# asterick for unpacking list and dict with function
# def test(a,b,c) -> b(*list1) OR def test(a,b,c) -> b(**dict1)

# UNPACKING CONTAINERS
first, *middle,last = [1,2,3,4,5,6,6]
print(first) # 1
print(middle) # [2, 3, 4, 5, 6] (will always output in list)
print(last) # 6

# * to merge iterables into list
my_tuple=(1,2,3)
my_list = [4,5,6]

new_list =[*my_tuple,*my_list]
print(new_list) #OP: [1, 2, 3, 4, 5, 6]

# MERGING TWO DICTS INTO ONE DICT
dict1 = dict(a=1,b=3)
dict2 = dict(a=2,b=4)

new_dict = {**dict1, **dict2}
print(new_dict) # {'a': 2, 'b': 4} only one of the above considererd if same key

dict1 = dict(a=1,b=3)
dict2 = dict(c=2,d=4)
new_dict = {**dict1, **dict2}
print(new_dict) # {'a': 1, 'b': 3, 'c': 2, 'd': 4}
