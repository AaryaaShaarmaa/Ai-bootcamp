import matplotlib.pyplot as plt


subjects = ["Math", "Physics", "Computer"]

aarya = [85, 90, 95]

friend = [80, 85, 90]


plt.figure(figsize=(7, 4)) # graph ko size set garcha



plt.plot(
    subjects,
    aarya,
    marker="o",
    label="Aarya"
)

plt.plot(
    subjects,
    friend,
    marker="o",
    label="Friend"
)


plt.title("Subject Marks Comparison")

plt.xlabel("Subjects")

plt.ylabel("Marks")


plt.grid() #graph ma lines add garcha for readability.

plt.legend()


plt.savefig("012_marks_comparison.png") #hamro pc ma save gardinxa


plt.show()