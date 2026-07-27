import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([5, 10, 15, 20, 25])

print("First Array:")
print(arr1)

print("\nSecond Array:")
print(arr2)

print("\nAddition:")
print(arr1 + arr2)

print("\nSubtraction:")
print(arr1 - arr2)

print("\nMultiplication:")
print(arr1 * arr2)

print("\nDivision:")
print(arr1 / arr2)

print("\nAdd 10:")
print(arr1 + 10)

print("\nMultiply by 2:")
print(arr1 * 2)

print("\nSquare:")
print(arr1 ** 2)

print("\nGreater than 25:")
print(arr1 > 25)

print("\nValues Greater than 25:")
print(arr1[arr1 > 25])

print("\nEven Numbers:")
print(arr1[arr1 % 2 == 0])