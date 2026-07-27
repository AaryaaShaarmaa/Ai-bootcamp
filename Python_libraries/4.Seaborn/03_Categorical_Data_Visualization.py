import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram","gu","su","pu"],
    "Department": [
        "Computer",
        "Computer",
        "Civil",
        "Electronics",
        "Computer",
        "Civil",
        "Civil",
        "Electronics"
    ],
    "Marks": [85, 90, 78, 95, 70, 65, 77, 89]
}


df = pd.DataFrame(data)


print("DataFrame:")
print(df)



print("\nCount Plot:") # category ko number count garcha

sns.countplot(
    x="Department",
    data=df
)

plt.title("Students in Each Department")

plt.show()



print("\nBox Plot:") # data ko spread ra outlier dekhauncha
# left of box q1 bichha ko median right ko q3

sns.boxplot(
    y="Marks",
    data=df
)

plt.title("Marks Distribution")

plt.show()



print("\nViolin Plot:") # data ko distribution shape dekhauncha

sns.violinplot(
    x="Department",
    y="Marks",
    data=df
)

plt.title("Department Marks Distribution")

plt.show()


'''
Countplot	           Counts categories
Boxplot	Shows          spread and outliers
Violinplot	           Shows distribution shape 

'''