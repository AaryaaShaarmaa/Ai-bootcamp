import pandas as pd


data = {
    "Name": ["Aarya", "Hari", "Sita"],
    "Age": [19, 20, 21],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


print("\nWriting CSV file:")

df.to_csv(
    "students.csv",
    index=False
)

# index=False le extra index column save hudaina


print("\nReading CSV file:")

df_csv = pd.read_csv("students.csv")

print(df_csv)


print("\nWriting Excel file:")

df.to_excel(
    "students.xlsx",
    index=False
)


# Excel file read garna openpyxl install garnu parcha
# pip install openpyxl

print("\nReading Excel file:")

df_excel = pd.read_excel("students.xlsx")

print(df_excel)