import requests
import json

r = requests.get('https://httpbin.org/get')
print(r.json())