import matplotlib.pyplot as plt


students = ["Aarya", "Hari", "Sita", "Gita"]

study_hours = [2, 4, 3, 6]

marks = [65, 85, 75, 95]


plt.scatter(
    study_hours,
    marks
)


plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")


plt.show()

#study hour badhyo = marks badhyo
'''
Scatter plots help us understand:

Relationship between two values
Patterns
Trends
Correlation

1.Positive correlation

When one increases, another also increases.


2.Negative correlation

One increases, another decreases.



3.No correlation

No clear pattern.
'''