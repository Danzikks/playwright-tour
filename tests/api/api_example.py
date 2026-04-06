import json
import requests

req = requests.get(
    url='https://api.github.com',
    headers={
        'Authorization': 'Bearer blabla'
    }
)
print(req.text)