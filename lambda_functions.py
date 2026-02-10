# LAMBDA Functions:
# lambda argument: expression (evaluate expression and return output)


def add_10(x):
    return x+10

# Lambda function with single argument
# aboove is similar to:
add_10_lambda=lambda x:x+10

print(add_10(10))
print(add_10_lambda(10)) #OP : 20

# Lambda function with multiple argument
multiply_func = lambda x,y: x*y

print(multiply_func(2,3)) #OP: 6

# Lambda function to sort list
list_2d = [(1,2),(15,1),(5,-1),(10,4)]
# Below will by default sort with first element of the tuple
list_2d_sorted = sorted(list_2d)
print(list_2d_sorted) # OP: [(1, 2), (5, -1), (10, 4), (15, 1)]

# NOW IF WE WANT TO sort with second element of the tuple
# Getting second element of tuple using lambda and passing it as key arg
list_2d_sorted = sorted(list_2d,key=lambda x:x[1])

print(list_2d_sorted) #OP: [(5, -1), (15, 1), (1, 2), (10, 4)]
