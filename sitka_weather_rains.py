import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

#	for index, column_header in enumerate(header_row):
#		print(index,column_header) #opady - index 3

	dates, rains = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		try:
			rain = float(row[3])
		except ValueError:
			print(f"Brak danych dla {current_date}.")
		else:
			dates.append(current_date)
			rains.append(rain)

#dane wykresu
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='blue', alpha = 0.5) 

#formatowanie wykresu
ax.set_title("Wielkość dziennych opadów w Sitka", fontsize = 20)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate() 
ax.set_ylabel('Opady (cm)', fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show()