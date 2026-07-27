import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram"],
    "Age": [19, 20, 18, 19, 21],
    "Study Hours": [3, 5, 2, 6, 4],
    "Attendance": [80, 90, 75, 95, 85],
    "Marks": [85, 95, 70, 98, 78]
}


df = pd.DataFrame(data)


print("First rows:")
print(df.head())


print("\nData Information:")
df.info()


print("\nStatistics:")
print(df.describe())


print("\nScatter Plot:")

sns.scatterplot(
    x="Study Hours",
    y="Marks",
    data=df
)

plt.title("Study Hours vs Marks")

plt.show()



print("\nHeatmap:")

correlation = df.drop(columns=["Name"]).corr()


sns.heatmap(
    correlation,
    annot=True
)

plt.title("Student Data Correlation")

plt.show()








'''
HERE:
1. Reading Real Dataset

We use Pandas:

pd.read_csv()

2. Understanding Data Before Visualization

Before making graphs, check the data.

First rows:
df.head() 

Information:
df.info()

Statistics:
df.describe()

These help us understand the dataset.


3. Handling Missing Data

Real datasets often have empty values.

Check:

df.isnull()

Count missing values:

df.isnull().sum()

Remove missing data:

df.dropna()

Fill missing data:

df.fillna()


4. Creating Visualizations From Real Data

Example dataset:

Name
Age
Study Hours
Attendance
Marks

We can analyze:

Marks distribution
sns.histplot()
Study Hours vs Marks
sns.scatterplot()
Correlation
sns.heatmap()


5.inding Insights

After visualization, we ask questions:

Example:

From scatter plot:
Do more study hours increase marks?
From heatmap:
Which factor affects marks most?
From histogram:
Where are most students marks located?
'''



'''

DATA ANALYSIS:

Read CSV
    ↓
Clean with Pandas
    ↓
Analyze with Seaborn
    ↓
Customize with Matplotlib
    ↓
Save report/dashboard

'''