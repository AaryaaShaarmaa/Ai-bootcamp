import pandas as pd


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita", "Ram"],
    "Age": [19, 20, 21, 18, 22],
    "Marks": [85, 90, 78, 95, 70],
    "City": ["Pokhara", "Kathmandu", "Chitwan", "Pokhara", "Kathmandu"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


print("\nMarks greater than 80:")
print(df[df["Marks"] > 80])


print("\nAge less than 20:")
print(df[df["Age"] < 20])


print("\nMultiple conditions:")
# & = AND, | = OR
# condition haru lai () vitra rakhne
print(df[
    (df["Marks"] > 80) &
    (df["Age"] > 18)
])


print("\nStudents from Pokhara:")
print(df[df["City"] == "Pokhara"])


print("\nSorting by Marks:")
print(df.sort_values("Marks"))


print("\nSorting by Marks descending:")
print(df.sort_values("Marks", ascending=False))


print("\nCounting values:")
print(df["City"].value_counts())