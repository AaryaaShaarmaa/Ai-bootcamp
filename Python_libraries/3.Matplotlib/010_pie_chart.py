import matplotlib.pyplot as plt


subjects = ["Math", "Physics", "Computer"]

marks = [40, 30, 30]


explode = [0.1, 0, 0] # first portion lai halka xuttai dinxa
#math halka bahira aaxa this is called exploaindg effect in pie chart

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%", #[ercentage value dinxa automatically sabai lai]
    explode=explode
)


plt.title("Marks Distribution")


plt.show()