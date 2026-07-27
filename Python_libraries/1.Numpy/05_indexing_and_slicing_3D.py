import numpy as np
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("\n3D Array:")
print(arr3)

print("\nFirst Element:")
print(arr3[0, 0, 0])

print("\nLast Element:")
print(arr3[1, 1, 1])

print("\nFirst Matrix:")
print(arr3[0])

print("\nSecond Matrix:")
print(arr3[1])

print("\nFirst Row of Second Matrix:")
print(arr3[1, 0])

print("\nSecond Column of First Matrix:")
print(arr3[0, :, 1])

print("\nAll First Elements:")
print(arr3[:, :, 0])

print("\nAll Second Elements:")
print(arr3[:, :, 1])

arr3[1, 0, 1] = 99

print("\nUpdated 3D Array:")
print(arr3)