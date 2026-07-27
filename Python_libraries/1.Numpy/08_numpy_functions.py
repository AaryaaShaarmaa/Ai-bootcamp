import numpy as np

arr = np.array([15, 8, 22, 8, 40, 15])

print("Array:")
print(arr)

print("\nSum:")
print(arr.sum())

print("\nAverage:")
print(arr.mean())

print("\nMaximum:")
print(arr.max())

print("\nMinimum:")
print(arr.min())

print("\nIndex of Maximum:")
print(arr.argmax())

print("\nIndex of Minimum:")
print(arr.argmin())

print("\nSorted Array:")
print(np.sort(arr))

print("\nUnique Values:")
print(np.unique(arr))

print("\nReshaped Array:")
arr2 = np.array([1, 2, 3, 4, 5, 6])
print(arr2.reshape(2, 3))

print("\nFlattened Array:")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.flatten())