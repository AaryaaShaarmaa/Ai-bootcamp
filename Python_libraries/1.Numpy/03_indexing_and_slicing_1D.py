import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array")
print(arr1)

print("\nFirst Element:")
print(arr1[0])

print("\nThird Element:")
print(arr1[2])

print("\nLast Element:")
print(arr1[-1])

print("\nElements from Index 1 to 3:")
print(arr1[1:4])

print("\nFirst Three Elements:")
print(arr1[:3])

print("\nFrom Index 2 to End:")
print(arr1[2:])

print("\nEvery Second Element:")
print(arr1[::2])

print("\nReverse Array:")
print(arr1[::-1])