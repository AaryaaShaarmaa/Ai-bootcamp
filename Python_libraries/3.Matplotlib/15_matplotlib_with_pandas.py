import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita"],
    "Marks": [85, 90, 78, 95]
}


df = pd.DataFrame(data)


print("DataFrame:")
print(df)


print("\nBar chart using DataFrame:")

plt.bar(
    df["Name"],
    df["Marks"]
)


plt.title("Student Marks")

plt.xlabel("Students")

plt.ylabel("Marks")


plt.show()



print("\nUsing df.plot():")


df.plot(
    x="Name",
    y="Marks",
    kind="bar"
)
'''
Kind=""
line → line graph
bar  → bar chart
hist → histogram
'''

plt.title("Student Performance")

plt.xlabel("Students")

plt.ylabel("Marks")


plt.grid()

plt.show()



'''
Readind CSV and visualizing :

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("students.csv")


df.plot(
    x="Name",
    y="Marks",
    kind="bar"
)


plt.show()



'''