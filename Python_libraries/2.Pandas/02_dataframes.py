import pandas as pd
data = {
    "Name": ["Ram", "Hari", "Sita"],
    "Age": [20, 19, 21],
    "Marks": [85, 90, 78]
}
#dataframes= row column bhako
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


print("\nSingle column:")
print(df["Name"])


print("\nMultiple columns:")
print(df[["Name", "Marks"]])


print("\nShape:")
print(df.shape)


print("\nColumn names:")
print(df.columns)


print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())


print("\nLast 5 rows:")
print(df.tail())


print("\nFirst 2 rows:")
print(df.head(2))


print("\nLast 2 rows:")
print(df.tail(2))

print("\nRows and columns:")
print(df.shape)


print("\nColumn names:")
print(df.columns)


print("\nData types:")
print(df.dtypes)


print("\nDataFrame information:")
df.info()


print("\nStatistical description:")
print(df.describe())