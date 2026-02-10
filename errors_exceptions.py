""" ERRORs -> happens before running the python code
eg:
a=5 print(a) (If we write both on same line will result in an error) (syntax errors)

Exceptions -> Even if statement is syntactically correct
but this may still cause error that is called exception

a=5+"ABC"
print(a) #OP : TypeError: unsupported operand type(s) for +: 'int' and 'str'

f=open("somefile.txt") # OP: FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

"""

# RAISING AN EXCEPTION
# x=-1
# if x<0:
#     raise Exception("Value of x cannot be less than zero")
# OP:
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/errors_execeptions.py", line 18, in <module>
#     raise Exception("Value of x cannot be less than zero")
# Exception: Value of x cannot be less than zero

# Raising assertion error using asserts
# x=-5
# assert x>0,'value of x cannot be negative'
# OP:
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/errors_execeptions.py", line 26, in <module>
#     assert x>0,'value of x cannot be negative'
# AssertionError: value of x cannot be negative

# Handling exceptions
try:
    a=5/0
    # above statement results in zerodivisionerror
except Exception as e:
    print('an error happened')

# Catching type of exception
# ITs a recommended practise to catch actual type of exception than just base exception
try:
    a=5/0
except ZeroDivisionError as zd:
    print("I am inside zero division error")
    print(zd)
# OP:
# I am inside zero division error
# division by zero