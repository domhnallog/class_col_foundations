import json
import requests
# api_token = 'your_api_token'
# api_url_base = 'https://swapi.co/api/people/1/?format=json'
response = requests.get('https://swapi.co/api/people/1/')
# print(response.text)
data = response.json()
# json.dumps(data, indent=2)
print(data['name'])
# print(data.keys()) 
print(data['films'])   # results come back as urls

### Endpoints for API
### /api/people/12


response = requests.get('https://swapi.co/api/films/2/')
film = response.json()
# print(film.keys())
print(film['title'])


print('-----------------------------------')
response = requests.get('https://swapi.co/api/people/1/')
person = response.json()
print(person['name'])

# for film_url in person['films']:
#   print(film_url)

for film_url in person['films']:
  print(film_url)
  print("Requesting the data from", film_url)
  response = requests.get(film_url)
  film = response.json()
  print(film['title'])