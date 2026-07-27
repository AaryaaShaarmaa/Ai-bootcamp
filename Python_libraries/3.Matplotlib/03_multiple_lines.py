import matplotlib.pyplot as plt


semester = [1, 2, 3, 4]

aarya = [3.2, 3.5, 3.7, 3.9]

friend = [3.0, 3.3, 3.6, 3.8]


plt.plot(
    semester,
    aarya,
    marker="o"
)

plt.plot(
    semester,
    friend,
    marker="o"
)

plt.legend()
plt.show()