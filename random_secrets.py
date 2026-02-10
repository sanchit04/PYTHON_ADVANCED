# Using seed random can regenerate same data thus making it in unsuitable for password generations
# in such cases we should use secrets module

import secrets
# Will generate true randoms which will be always below 10 i.e. 0 to 9
print(secrets.randbelow(10))

# Generates 0-15 value that is becase -> 1111 -> is highest value for length of 4
print(secrets.randbits(4))
# OP : 11

# accessing randomly
list1=[1,2,3,4]
print(secrets.choice(list1)) # Truly randomly selection of elements! # OP: 4