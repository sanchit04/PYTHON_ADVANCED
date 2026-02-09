# Strings are ordered, immutable, text representation and an iterable object
string1=str("BC")
print(string1)
string1="Hello World!"
print(string1)

## Multiline string
string1="""Hello
I am here"""
print(string1)

## String with escape characters
string1 = 'Hello World\'s'
print(string1) #OP -> Hello World's
#OR
string1 = "Hello World's" #(double quotes inside single quotes then no escape character needed)
print(string1) #OP -> Hello World's

#Accessing Strings
# using index ->
string1 = "HelloWorld!"
print(string1[0]) #OP -> H

# using negative index ->
print(string1[-1]) #OP -> !

# slicing strings (same as list, tuple slicing)
print(string1[0:5]) #OP -> Hello
print(string1[4::-1]) #OP -> olleH
print(string1[5:]) #OP -> World!
print(string1[::-1]) #OP -> (Reverses the string) !dlroWolleH

#UPDATING A STRING: Not possible since string is immutable
# string1[0]="TH"
#OP TypeError: 'str' object does not support item assignment

#Concatenating a string (this creates a new string thus its supported)
string1="Hello"
string2="World"
string3 = string1 +" "+ string2
print(string3)

#Iterating a string
for i in string3:
    print(i)
# OP:
# H
# e
# l
# l
# o
#
# W
# o
# r
# l
# d

#Check for existing in string:
if 'H' in string1:
    print('H is present')

if 'Hello' in string1:#(Case sensitive)
    print('Hello is present')

# Removing whitespaces from string
string3='    hello   world   '
print(string3.strip()) # strip removes white spaces from LHS and RHS only no middle white spaces are removed

print(string3)
string4=string3.strip() # storing in a variable since strip wont affect existing string.
print(string4)

#LOWER and UPPER in string
print(string4.upper())
print(string4.lower())

#StartsWith

print(string4.startswith("H")) # return Boolean (case sensitive) OP False
print(string4.endswith("d")) # returns Boolean OP True

# Find INDEX of the character

print(string4.find('l')) # gives the first index found for the character OP 2
print(string4.find('L')) # Returns -1 if the character is not found in the string

# Count number characters in a string
print(string4.count('l')) # OP 3
print(string4.count('L')) # OP 0 case sensitive

# Replace in string
my_string_replace = string4.replace("world","universe")
print(my_string_replace) #OP hello   universe

#If the existing word does not exist it will do nothing
my_string_replace = string4.replace("Sanchit","universe")
print(my_string_replace) #OP hello   world

