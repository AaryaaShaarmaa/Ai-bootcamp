import numpy as np

print("Random Decimal Numbers:")
print(np.random.rand(5))

print("\nRandom Integers:")
print(np.random.randint(1, 101, 5))

print("\nRandom 2D Array:")
print(np.random.randint(1, 10, (3, 3)))

print("\nRandom Choice:")
colors = np.array(["Red", "Blue", "Green", "Yellow"])
print(np.random.choice(colors))

print("\nThree Random Choices:")
print(np.random.choice(colors, 3))

print("\nUsing Seed:")
np.random.seed(10)
print(np.random.randint(1, 11, 5))