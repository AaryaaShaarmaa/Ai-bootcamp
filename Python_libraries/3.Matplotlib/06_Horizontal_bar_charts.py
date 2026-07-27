import matplotlib.pyplot as plt


cities = ["Kathmandu", "Pokhara", "Chitwan"]

population = [100, 80, 60]


plt.barh(                  
    cities,
    population
)
for i in range(len(population)):
    #syntax : plt.text(x_position, y_position, "what to write")
    plt.text(
        population[i],i,population[i]
    )

plt.show()