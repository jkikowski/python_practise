import matplotlib.pyplot as plt

x_values=range(1,5000)
y_values=[x**3 for x in x_values]

plt.style.use('bmh')
fig,ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues)

ax.set_title("Kwadrat liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

#plt.show()
plt.savefig('szesciany.png', bbox_inches='tight')