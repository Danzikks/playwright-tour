from urllib import response

from requests import Request, Session

req = Request(
    'POST',
    'https://api.github.com',
    headers={
        'Authorization': 'token ghp_your_token',
    },
    json={
        'name': 'test',
        'body': 'test'
    }
)

session = Session()
prepared = req.prepare()
response = session.send(prepared)
print(response)