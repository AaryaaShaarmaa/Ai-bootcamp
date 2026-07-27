import matplotlib.pyplot as plt


students = ["Aarya", "Hari", "Sita", "Gita", "Ram" , "nuro","dhiru"]

marks = [85, 90, 78, 95, 70, 71, 72]


plt.hist(
    marks,
    bins=5
)
# yo le marks lai 5 ota group (range) ma divide garcha
#for eg here from (70 to 95 5 ota group)
#70 - 75 = 3 jana 
#75 to 80 = 1 jana
#80 to 85 =0 jana and so on
# ani harek range ma kati ota marks paryo bhanera count garcha
# histogram le individual student dekhaudaina


plt.title("Student Marks Distribution")



plt.xlabel("Marks")



plt.ylabel("Frequency")
# yo le y-axis ma kati jana student tyo range ma chan bhanera dekhauncha


plt.show()
