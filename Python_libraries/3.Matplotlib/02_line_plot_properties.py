import matplotlib.pyplot as plt


semesters = [1, 2, 3, 4]

cgpa = [3.2, 3.5, 3.7, 3.9]


plt.plot(
    semesters,
    cgpa,
    marker="*", #tyo dot at x,y point
    linestyle="--", 
    linewidth=2, 
    markersize=8  #marker ko size
)


plt.title("CGPA Progress")
plt.xlabel("Semester")
plt.ylabel("CGPA")


plt.show()