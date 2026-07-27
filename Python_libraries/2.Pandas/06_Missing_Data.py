import pandas as pd


data = {
    "Name": ["Aarya", "Hari", "Sita", "Gita"],
    "Age": [19, None, 21, 18],
    "Marks": [85, 90, None, 95]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


print("\nChecking missing values:")
print(df.isnull())


print("\nTotal missing values:")
print(df.isnull().sum())


print("\nFilling missing values:")

df["Age"] = df["Age"].fillna(20)

print(df)


print("\nFilling all missing values:")

df.fillna(0, inplace=True)

# inplace=True le original dataframe change garcha

print(df)


print("\nRemoving rows with missing values:")

data = {
    "Name": ["Aarya", "Hari", "Sita"],
    "Marks": [85, None, 90]
}

df2 = pd.DataFrame(data)

print(df2)


df2.dropna(inplace=True)

print("\nAfter dropna:")
print(df2)