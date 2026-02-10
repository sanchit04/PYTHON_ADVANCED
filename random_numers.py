# RANDOM use to generate pseudo random numbers
# pseudo randoms -> numbers which look randoms but are reproducible

import random

# Generate random float from range 0-1
print(random.random()) #OP 0.23437981298246002

# Generate random float based on a range we provide eg 1 to 10
print(random.uniform(0,10)) #OP 4.432831165700667

# Generate random int based on a range (includes upper bound)
print(random.randint(0,10)) #OP 10

# Generate random int based on range but dont include upper bound
print(random.randrange(0,10)) #OP 4

# ACCESSING RANDOM Values
list1=[1,2,3,4,4,5,5,5,6]

#pick any single element from the list
print(random.choice(list1)) # 4

#To pick multiple elements (In our case will pick 3)
# sample will always pick unique random elements it cannot return duplicates
print(random.sample(list1,3)) # [5, 2, 1]

# To return duplicate multiple randome elements
print(random.choices(list1,k=3)) # OP : [6, 5, 5]

# To shuffle randomly elements of the list
random.shuffle(list1)
print(list1) # SHUFFLES THE EXISTING LIST

