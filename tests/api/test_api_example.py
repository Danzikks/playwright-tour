import json

import allure
import jsonschema
import pytest
from pytest_check import check
import requests

@allure.title('Тестовый запрос в апи')
def test_send_api():

    req = requests.get(
        url='https://jsonplaceholder.typicode.com/posts',
    )
    response_json = req.json()
    assert req.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    for item in response_json:
        jsonschema.validate(item, schema)

def test_create_post():
    req = requests.post(
        url='https://jsonplaceholder.typicode.com/posts/', )

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
        }
    }
    jsonschema.validate(req.json(), schema)
    assert req.status_code == 201