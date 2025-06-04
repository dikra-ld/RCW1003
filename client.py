import requests

url = 'https://rcw1003-dikra-hyfme3c7gubmdmet.canadaeast-01.azurewebsites.net/test'
response = requests.get(url)
data = response.json()
print(data['message']) 
