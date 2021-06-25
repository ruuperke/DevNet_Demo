import requests

response = requests.get('http://api.icndb.com/jokes/random?exclude=explicit')
print(response.text)

data = response.json()
print(data['value']['joke'])