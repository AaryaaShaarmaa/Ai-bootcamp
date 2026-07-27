import pandas as pd


data = {
    "Name": ["Ram", "Hari", "Sita", "Gita"],
    "Age": [20, 19, 21, 18],
    "Marks": [85, 90, 78, 95],
    "City": ["Pokhara", "Kathmandu", "Chitwan", "Pokhara"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


print("\nSelecting single column:")
print(df["Name"])


print("\nSelecting multiple columns:")
print(df[["Name", "Marks"]])


print("\nSelecting row using loc:")
print(df.loc[2])


print("\nSelecting multiple rows using loc:")
# loc ma start ra end dubai include huncha
print(df.loc[1:3])


print("\nSelecting row and column using loc:")
print(df.loc[1:3, ["Name", "Marks"]])


print("\nSelecting row using iloc:")
print(df.iloc[2])


print("\nSelecting multiple rows using iloc:")
# iloc ma end include hudaina
print(df.iloc[1:3])


print("\nSelecting row and column using iloc:")
print(df.iloc[1:3, 0:2])