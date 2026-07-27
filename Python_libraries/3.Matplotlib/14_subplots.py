import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar"]

sales = [20, 30, 25]

profit = [5, 10, 8]


fig, ax = plt.subplots(1, 2)
#fig - represents the whole figure.
#ax - represents the graph area.

ax[0].plot(months, sales)

ax[0].set_title("Sales")


ax[1].plot(months, profit)

ax[1].set_title("Profit")


plt.show()

'''
subplot()	                      subplots()
Simple	                          More flexible
Creates one graph at a time   	 Creates multiple axes together
Good for beginners	             Used more in projects

'''