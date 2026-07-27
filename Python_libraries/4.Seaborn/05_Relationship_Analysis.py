import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram"],
    "Study Hours": [3, 5, 2, 6, 4],
    "Marks": [85, 95, 70, 90, 78],
    "Department": [
        "Computer",
        "Computer",
        "Civil",
        "Computer",
        "Civil"
    ]
}


df = pd.DataFrame(data)


print("DataFrame:")
print(df)



print("\nScatter Plot with Hue:")

sns.scatterplot(
    x="Study Hours",
    y="Marks",
    hue="Department", # category anusar data separate garcha 
    #i.e Computer ra Civil lai different dekhauncha
    data=df
)


plt.title("Study Hours vs Marks")

plt.show()



print("\nPair Plot:") # sabai numerical columns ko relation ekai choti dekhauncha
#"Show me every possible pair in my dataset.
#sabai lai sabai sanga compare garera dekhaidinxa
sns.pairplot( 
    df.drop(columns=["Name", "Department"])
)


plt.show()