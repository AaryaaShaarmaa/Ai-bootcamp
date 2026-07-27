import matplotlib.pyplot as plt


students = ["Aarya", "Hari", "Sita", "Gita"]

marks = [85, 90, 78, 95]


plt.bar(students,
        marks,
        color="green", #gives color
        width=0.5) #gives width of bar


plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

for i in range(len(marks)): #We can show values above bars using text()
    # syntax : plt.text(x_position, y_position, "what to write")
    plt.text(
        i,
        marks[i],
        marks[i]
    )
plt.show()