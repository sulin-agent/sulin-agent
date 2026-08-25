import requests

m = requests.get('https://jsonplaceholder.typicode.com/users/2')
date = m.json()
print(date['name'])
print(date["username"])
print(date["company"]["name"])
print(date["address"]["geo"]["lng"])