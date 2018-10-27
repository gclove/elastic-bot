import requests
r = requests.get('https://api.github.com/repos/elastic/elasticsearch/tags')
print(r.json()[0]['name'][1:])
