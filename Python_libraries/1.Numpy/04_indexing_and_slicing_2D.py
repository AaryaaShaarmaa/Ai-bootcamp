import numpy as np
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Array")
print(arr2)

print("\nElement at Row 2 Column 3:")
print(arr2[1, 2])

print("\nFirst Row:")
print(arr2[0])

print("\nLast Row:")
print(arr2[-1])

print("\nSecond Column:")
print(arr2[:, 1])

print("\nFirst Two Columns:")
print(arr2[:, 0:2])

print("\nBottom Right 2x2 Matrix:")
print(arr2[1:, 1:])

arr2[0, 1] = 99

print("\nUpdated Array:")
print(arr2)