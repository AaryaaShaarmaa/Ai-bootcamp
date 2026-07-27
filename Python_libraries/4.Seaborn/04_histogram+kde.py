import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram"],
    "Marks": [85, 90, 78, 95, 70]
}


df = pd.DataFrame(data)


print("DataFrame:")
print(df)


print("\nHistogram:") # data ko range ma divide garera frequency dekhauncha

sns.histplot(
    x="Marks",
    data=df,
    bins=5 # data lai kati group ma divide garne bhancha
)

plt.title("Marks Distribution")

plt.xlabel("Marks")

plt.ylabel("Frequency")

plt.show()



print("\nHistogram with KDE:")

sns.histplot(
    x="Marks",
    data=df,
    kde=True # smooth distribution line add garcha in histogram
)

plt.title("Marks Distribution with KDE")

plt.show()



print("\nKDE Plot:")

sns.kdeplot(
    df["Marks"]
)

plt.title("Marks Density")

plt.show()

'''
    Histogram	          KDE (Kernel Density Estimate.)
Uses bars	                 Uses smooth curve
Shows frequency	             Shows distribution shape
'''