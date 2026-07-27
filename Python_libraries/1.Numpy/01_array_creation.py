import numpy as np
# Creating array from list
arr1 = np.array([10, 20, 30, 40, 50])
print("\n1. Array using np.array()")
print(arr1)

# Array of zeros
arr2 = np.zeros((2, 3))
print("\n2. Array of Zeros")
print(arr2)

# Array of ones
arr3 = np.ones((3, 2))
print("\n3. Array of Ones")
print(arr3)

# Using arange
arr4 = np.arange(1, 11, 2)
print("\n4. Array using np.arange()")
print(arr4)

# Using linspace
arr5 = np.linspace(0, 100, 5)
print("\n5. Array using np.linspace()")
print(arr5)

# Identity Matrix
arr6 = np.eye(4)
print("\n6. Identity Matrix")
print(arr6)

# Random decimal numbers
arr7 = np.random.rand(5)
print("\n7. Random Decimal Numbers")
print(arr7)

# Random integers
arr8 = np.random.randint(1, 101, 5)
print("\n8. Random Integers")
print(arr8)
