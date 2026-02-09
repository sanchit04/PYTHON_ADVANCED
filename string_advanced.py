#SPLIT FUNCTION in strings (RETURNS LIST OF STRING)

my_string = "How,are,you,doing"
my_list = my_string.split(",")
print(my_list)
print(len(my_list))
print(type(my_list))
#OP:
# ['How', 'are', 'you', 'doing']
# 4
# <class 'list'>

#If we split on something which does not exist
# it will still create a list but entire string as one element in the list

my_list = my_string.split(" ")
print(my_list)
print(len(my_list))
print(type(my_list))
#OP:
# ['How,are,you,doing']
# 1
# <class 'list'>

# Converting list to a string
list1 = ["how","are","you"]
string1 = " ".join(list1)
print(string1)

# FORMATTING STRING

# %, .format(), f_strings

# 1) using %
a="Tom"
mystring = "my name is %s" %a
print(mystring) # my name is Tom

f=3.123456676777
mystring="my value is %f" %f
print(mystring) #my value is 3.123457 by default shows upto 6 only

mystring ="my value is %.2F" %f
print(mystring) # my value is 3.12

# 2) .format
var_f = 3.123456676777
mystring = "my value is {:.2F}".format(var_f)
print(mystring) # my value is 3.12

var_string = "sanchit"
mystring="my value is {}".format(var_string)
print(mystring) #my value is sanchit

# 3) f_strings since python3.6
var1=("abc")
print(f"my value is:{var1}")
