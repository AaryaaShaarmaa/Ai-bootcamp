import matplotlib.pyplot as plt
import numpy as np


students = ["Aarya", "Hari", "Sita"]

semester1 = [80, 85, 90]
semester2 = [85, 90, 95]


x = np.arange(len(students))
# yo le students ko position number banaucha
# Aarya = 0, Hari = 1, Sita = 2
# bar lai place garna yesto number chaincha

width = 0.35



plt.bar(
    x - width/2,
    semester1,
    width,
    label="Semester 1"
)
# yele le Semester 1 ko bar banauncha
# x - width/2 le bar lai ali left tira shift garcha
# kina bhane arko semester ko bar right side ma rakhnu parcha


plt.bar(
    x + width/2,
    semester2,
    width,
    label="Semester 2"
)
# yo le Semester 2 ko bar banauncha
# x + width/2 le bar lai ali right tira shift garcha
# aba dui ota bar eutai thau ma overlap hudaina


plt.xticks(
    x,
    students
)
# yo le x-axis ma 0,1,2 ko satta student ko naam dekhauncha
# 0 ko thau ma Aarya, 1 ko thau ma Hari, 2 ko thau ma Sita


plt.legend()



plt.show()
