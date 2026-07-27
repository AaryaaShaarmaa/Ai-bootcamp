#series means data in single line 
import pandas as pd


numbers = [10, 20, 30, 40]

series = pd.Series(numbers)

print("Series:")
print(series)


marks = pd.Series(
    [85, 90, 78],
    index=["Ram", "Hari", "Sita"]
)

print("\nSeries with custom index:")
print(marks)
