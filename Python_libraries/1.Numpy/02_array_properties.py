import numpy as np


arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\nArray:")
print(arr)

print("\nNumber of Dimensions:")
print(arr.ndim)

print("\nShape:")
print(arr.shape)

print("\nSize:")
print(arr.size)

print("\nData Type:")
print(arr.dtype)

print("\nChanging Data Type to Float")
arr = arr.astype(float)

print(arr)
print(arr.dtype)

