import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

	rw = RandomWalk(5000)
	rw.fill_walk()

	plt.style.use('classic')
	fig,ax = plt.subplots() 
	point_numbers=range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=3)
	#ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none',s=1)

	#podkreślenie pierwszego i ostatniegu punktu losowego
	#ax.scatter(0, 0, c='green', edgecolor='none',s=100)
	#ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',  edgecolor='none',s=100)

	#ukrywanie osi
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	
	keep_running = input("Utworzć kolejne błądzenie losowe? (t/n): ")
	if keep_running == 'n':
		break  