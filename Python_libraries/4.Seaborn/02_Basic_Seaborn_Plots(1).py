import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita"],
    "Marks": [85, 90, 78, 95],
    "Study Hours": [3, 5, 2, 6]
}

df = pd.DataFrame(data)


print("DataFrame:")
print(df)


print("\nLine Plot:")

sns.lineplot(
    x="Name",
    y="Marks",
    data=df
)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()



print("\nScatter Plot:")

sns.scatterplot(
    x="Study Hours",
    y="Marks",
    data=df
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()



print("\nBar Plot:")

sns.barplot(
    x="Name",
    y="Marks",
    data=df
)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()



'''
line Plot	             Change over time
Scatter Plot	         Relationship between values
Bar Plot 	             Compare categories
'''