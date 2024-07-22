import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Dimensions in Arrays

# 0D Arrays
arr1 = np.array(42)
print(arr1)

# I-D Arrays
arr2 = np.array([1, 2, 3, 4, 5])
print(arr2)

# 2-D Arrays
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3)


# Accessing Arrays
#Accessing in 1-D Array
print(arr2[2])

#Accessing in 2-D Array
print(arr3[1, 2])

#Accessing in 3-D Array