import json
import jsonschema
from pytest_check import check
import requests

req = requests.get(
    url='https://api.github.com',
    headers={
        'Authorization': 'Bearer blabla'
    }
)
print(req.text)