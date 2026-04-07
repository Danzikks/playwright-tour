import json
import jsonschema
import pytest
from pytest_check import check
import requests


def test_send_api():
    req = requests.get(
        url='https://api.github.com',
        headers={
            'Authorization': 'Bearer blabla'
        }
    )
    print(req.text)