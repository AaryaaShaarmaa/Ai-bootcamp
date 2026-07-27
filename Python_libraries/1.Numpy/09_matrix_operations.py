import numpy as np

matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Addition:")
print(matrix1 + matrix2)

print("\nMatrix Subtraction:")
print(matrix1 - matrix2)

print("\nElement-wise Multiplication:")
print(matrix1 * matrix2)

print("\nMatrix Multiplication:")
print(matrix1 @ matrix2)

print("\nTranspose of Matrix 1:")
print(matrix1.T)

print("\nTranspose of Matrix 2:")
print(matrix2.T)