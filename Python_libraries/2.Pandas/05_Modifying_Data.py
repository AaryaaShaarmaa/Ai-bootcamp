import pandas as pd


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita"],
    "Age": [19, 20, 21, 18],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


print("\nAdding new column:")

df["Result"] = "Pass"

print(df)


print("\nUpdating values:")

df.loc[df["Marks"] < 80, "Result"] = "Fail"

print(df)


print("\nRenaming column:")

df.rename(
    columns={"Marks": "Score"},
    inplace=True
)

# inplace=True le original dataframe change garcha

print(df)


print("\nDropping column:")

df.drop(
    "Result",
    axis=1,
    inplace=True
)

# axis=1 means column, axis=0 means row

print(df)


print("\nDropping row:")

df.drop(
    0,
    axis=0,
    inplace=True
)

print(df)