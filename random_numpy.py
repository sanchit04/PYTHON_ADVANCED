import numpy as np

print(np.random.rand(3)) #OP: [0.50233122 0.54717979 0.39257342] (Generate floats only) returns 1D array

# Generates 3D (3*3) Random array of fliats
print(np.random.rand(3,3))
#OP:

# [[0.72486002 0.23617753 0.67210034]
#  [0.24956548 0.65127835 0.70316007]
#  [0.04125677 0.32876391 0.38409334]]

# Generates 3*3 random int generated of range 0 to 10 array
print(np.random.randint(0,10,(3,3)))
# OP:
# [[6 8 7]
#  [8 1 7]
#  [6 4 5]]

# NUMPY ARRAY random shuffle
arr = np.array([[1,2,3],[4,5,6],[7,9,9]])
print(arr)
#OP:
# [[1 2 3]
#  [4 5 6]
#  [7 9 9]]
# Will shuffle array position only it wont shuffle elements inside array!
np.random.shuffle(arr)
print(arr)
#OP:
# [[4 5 6]
#  [7 9 9]
#  [1 2 3]]

