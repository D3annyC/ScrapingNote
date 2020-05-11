import requests
import json

URL = 'https://httpbin.org/'
form_data = {'gender': 'M', 'page': '1'}

# get test
getrespon = requests.get(URL+'get')
print(getrespon.text)

print('-'*40)

r = requests.get(URL, params=form_data)
print(r.url)
