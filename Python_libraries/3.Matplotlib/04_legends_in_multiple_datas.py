import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [1, 4, 9], label="Squares")
plt.plot([1, 2, 3], [1, 8, 27], label="Cubes")
plt.legend() 
# Displays the legend automatically 
#(side ko baksa top left) used with lable
plt.show()
