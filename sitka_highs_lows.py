import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f) 
	header_row = next(reader) 
	#print(header_row)

	#for index, column_header in enumerate(header_row): 
	#	print(index,column_header)

	#pobieranie maksymalanych temperatur z pliku
	dates, highs, lows =[], [], []
	for row in reader:
		current_date = datetime.strptime(row[2], "%Y-%m-%d") 
		high = int(row[5]) 
		low = int(row[6])
		dates.append(current_date)
		highs.append(high)
		lows.append(low)
		
""" zrobiłem z tego blok komentarza żeby w pliku death_valley... nie wyświetlał się drugi wykres
#dane wykresu
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha = 0.5) #wyświetla podane dane w określonym kolorze
ax.plot(dates, lows, c='blue', alpha = 0.5) #alpha określa przezroczystosć koloru od 0 do 1
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) #dates podajem jako serie wartości do osi x a highs i lows do Y

#formatowanie wykresu
ax.set_title("Najwyższa i najniższa temp. w Sitka dnia - 2018", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate() #wyświetla etykiety (podane dane) ukośnie - żeby nie nachodziły na siebie
ax.set_ylabel('Temperatura (F)', fontsize = 16)
ax.tick_params(axis='both', which = 'major', labelsize = 16)

plt.show() - wywołanie wykresu
"""