import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita"],
    "Marks": [85, 90, 78, 95]
}


df = pd.DataFrame(data)


print("DataFrame:")
print(df)


sns.set_theme() # overall seaborn appearance set garcha


sns.set_style("whitegrid") # graph ko background style change garcha


plt.figure(figsize=(8,4)) # graph ko size control garcha


sns.barplot(
    x="Name",
    y="Marks",
    data=df
)


plt.title("Student Marks Comparison")

plt.xlabel("Students")

plt.ylabel("Marks")


plt.show()