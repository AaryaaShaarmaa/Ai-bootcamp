import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram"],
    "Study Hours": [3, 5, 2, 6, 4],
    "Attendance": [80, 90, 70, 95, 75],
    "Marks": [85, 95, 70, 98, 78]
}


df = pd.DataFrame(data)


print("DataFrame:")
print(df)


correlation = df.drop(columns=["Name"]).corr() #name chaiyena
# numerical columns ko relation calculate garcha


print("\nCorrelation Matrix:")
print(correlation)


sns.heatmap(   # correlation lai visual form ma dekhauncha
    correlation,
    annot=True # heatmap bhitra value dekhauncha
)


plt.title("Student Data Correlation")


plt.show()