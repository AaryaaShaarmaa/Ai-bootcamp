import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar"]

sales = [20, 30, 25]

profit = [5, 10, 8]


plt.subplot(1, 3, 1) 
'''
1 row
3 columns
first graph
'''

plt.plot(months, sales)

plt.title("Sales")


plt.subplot(1, 2, 2)
'''
1 row
2 columns
second graph
'''

plt.plot(months, profit)

plt.title("Profit")


plt.show()