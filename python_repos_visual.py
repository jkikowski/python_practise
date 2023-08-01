import requests

from plotly.graph_objs import Bar
from plotly import offline

#wywołanie API i zapisanie odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} #definiujesz z jakiej wersji API chcesz skorzystać (definiujesz wywołania)
r = requests.get(url, headers = headers) #łączy z API (wywołuje)
print(f"Kod stanu: {r.status_code}") #wyświetlenie czy odpowiednio połączył się z API

#umieszczenie potrzebnych danych w zmiennych
response_dict = r.json() #wszystkie dane z GitHuba w zmiennej response_dict
repo_dicts = response_dict['items'] #przechwytujemy tylko część pobranych danych
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts: #pętla zapełnia odpowiednimi danymi dwie listy, które przekierujemy na osie x i y
	repo_name = repo_dict['name']
	repo_url = repo_dict['html_url']
	repo_link = f"<a href='{repo_url}>{repo_name}</a>'"
	repo_links.append(repo_link)

	stars.append(repo_dict['stargazers_count'])

	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br />{description}" #plotly pozwala na kod html w elementach tekstowych
	labels.append(label)

#utworzenie wizualizacji
data = [{ #podanie danych do wykresu
	'type': 'bar', #jakiego typu wyświetli się wykres
	'x': repo_links, #dane dla osi x
	'y': stars, #dane dla osi y
	'hovertext': labels,
	'marker':{ #marker odpowiada za wygląd słupków
		'color':'rgb(60, 100, 150)',
		'line':{'width':1.5, 'color': 'rgb(25,25,25)'}
	},
	'opacity': 0.6,
}]

my_layout = { #opisy do wykresu
	'title': 'Oznaczone największą liczbą gwiazdek projekty Pythona na GitHub`ie',
	'titlefont': {'size':28}, #zmienia rozmiar czcionki głównego tytułu
	'xaxis': {
		'title': 'Repozytorium',
		'titlefont': {'size':24},
		'tickfont': {'size': 14}
	},
	'yaxis': {
		'title': 'Gwiazdki',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data':data, 'layout': my_layout} #połączenie skąd wykres ma wziąc jakie dane
offline.plot(fig,filename='python_repos.html') #wywołanie wykresu