import sitka_highs_lows
import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

#	for index, column_header in enumerate(header_row):
#		print(index,column_header)

	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d")
		try:
			high = int(row[4])
			low = int(row[5])
		except ValueError:
			print(f"Brak danych dla {current_date}.")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#dane wykresu z death valley
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5) 
ax.plot(dates, lows, c='blue', alpha = 0.5) 
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) 

#dane z sitka
ax.plot(sitka_highs_lows.dates, sitka_highs_lows.highs, c='purple', alpha = 0.5) 
ax.plot(sitka_highs_lows.dates, sitka_highs_lows.lows, c='green', alpha = 0.5) 
ax.fill_between(sitka_highs_lows.dates, sitka_highs_lows.highs, sitka_highs_lows.lows, facecolor='green', alpha=0.1) 

#formatowanie wykresu
ax.set_title("Najwyższa i najniższa temp. dnia - 2018\n Dolina Śmierci Kalifornia", fontsize = 20)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate() #wyświetla etykiety (podane dane) ukośnie - żeby nie nachodziły na siebie
ax.set_ylabel('Temperatura (F)', fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show()