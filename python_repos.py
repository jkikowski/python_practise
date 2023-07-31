import requests

#wywołanie API i zapisanie odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' 
headers = {'Accept': 'application/vnd.github.v3+json'} 
r = requests.get(url, headers = headers) 
print(f"Kod stanu: {r.status_code}")

#umieszenie odpowiedzi API w zmiennej
response_dict = r.json()
print(f"Liczba repozytoriów: {response_dict['total_count']}") 

repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytowiów: {len(repo_dicts)}")

#analiza pierwszego repozytorium
repo_dict = repo_dicts[0]
#print(f'\nKlucze: {len(repo_dict)}') #pętla pokazujące jakie klucze informacji zawiera każde repozytorium
#for key in sorted(repo_dict.keys()): 
#	print(key)

print('\nWybrane informacje o pierwszym repozytirum:')
print(f"Nazwa: {repo_dict['name']}")
print(f"Właściciel: {repo_dict['owner'] ['login']}")
print(f"Gwiazdki: {repo_dict['stargazers_count']}")
print(f"Repozytorium: {repo_dict['html_url']}")
print(f"Uworzone w: {repo_dict['created_at']}")
print(f"Uaktualnione: {repo_dict['updated_at']}")
print(f"Opis: {repo_dict['description']}")