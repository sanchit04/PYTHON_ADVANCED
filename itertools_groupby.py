from itertools import groupby

# QUESTION: GROUP ALL ELEMENTS which are less than 3
# IMPORTANT CONCEPT ABOUT ITERTOOLS ONCE THE DATA IS CONSUMED THEN ITS NOT SHOWN AGAIN
list1=[1,5,2,4]
result_dict = groupby(list1,key=lambda x: x<3)
#print(list(result_dict)) # IF WE PRINT HERE THEN FOR LOOP WILL BE EMPTY!!

#OP
#[(True, <itertools._grouper object at 0x102dc1100>), (False, <itertools._grouper object at 0x102de6fa0>), (True, <itertools._grouper object at 0x102e01250>), (False, <itertools._grouper object at 0x102e010d0>)]

for key,value in result_dict:
    print(key,list(value))

#OP: WHY theres no group by?
# True [1]
# False [5]
# True [2]
# False [4]

# iter tools groupby only works if next element can belong to same group after evaluation then only its merged
# for eg in our case 1 TRUE, 5 FALSE (its not beloging to same group)
# if we had 1 True, 2 True (in this case it would have merged)

list1.sort()
print(list1)

result_dict = groupby(list1,key=lambda x: x<3)
for key,value in result_dict:
    print(key,list(value))

#OP: (since now we sorted and then group by thus its working as per expectation of group by)
# True [1, 2]
# False [4, 5]

