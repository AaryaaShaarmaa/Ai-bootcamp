import pandas as pd


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram"],
    "Age": [19, 20, 21, 18, 22],
    "Department": ["Computer", "Computer", "IT", "IT", "Computer"],
    "Marks": [85, 90, 78, 95, 70]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


print("\nAverage marks by department:")

print(
    df.groupby("Department")["Marks"].mean()
)


print("\nTotal marks by department:")

print(
    df.groupby("Department")["Marks"].sum()
)


print("\nNumber of students in each department:")

print(
    df.groupby("Department")["Marks"].count()
)


print("\nHighest marks in each department:")

print(
    df.groupby("Department")["Marks"].max()
)


print("\nLowest marks in each department:")

print(
    df.groupby("Department")["Marks"].min()
)


print("\nMultiple calculations using agg:")

print(
    df.groupby("Department")["Marks"].agg(
        ["mean", "sum", "max", "min"]
    )
)


print("\nGrouping using multiple columns:")

print(
    df.groupby(["Department", "Age"])["Marks"].mean()
)


print("\nReset index:")

result = df.groupby("Department")["Marks"].mean()

# reset_index le grouped result lai normal dataframe banaucha

result = result.reset_index()

print(result)