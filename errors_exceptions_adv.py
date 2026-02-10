# TRY, EXCEPT, ELSE AND FINALLY CLAUSE
# TRY: Executed always
# EXCEPT : If any exception occurs then this block will be executed
# ELSE : Executed only when no exception occurs
# FINALLY: Will always execute irrespective of exception occurred or not

try:
    a=5/1
    b=a+4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine!")
finally:
    print("cleaning up everything!")

# DEFINING your own exceptions

class ValueTooHighError(Exception):
    pass

# We should not use lambda expressions when using to raise exceptions use normal functions instead
#test_value = lambda x: if x>10 raise ValueTooHighError

def test_value(x):
    if x>10:
        raise ValueTooHighError(f"x:{x} value is greater than 10!")

print(test_value(30))

#OP:
# Traceback (most recent call last):
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/errors_exceptions_adv.py", line 31, in <module>
#     print(test_value(30))
#   File "/Users/sanchitgawde/PycharmProjects/PYTHON_ADVANCED/errors_exceptions_adv.py", line 29, in test_value
#     raise ValueTooHighError(f"x:{x} value is greater than 10!")
# __main__.ValueTooHighError: x:30 value is greater than 10!
