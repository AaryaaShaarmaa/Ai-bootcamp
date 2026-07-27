import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data = {
    "Name": ["Aarya", "Hari", "Sita"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)


sns.barplot(
    x="Name",
    y="Marks",
    data=df
)


plt.show()