import json
import requests

def get_request(url):
    r = requests.get(url)
    return r.content

def post_request(url, payload):
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return r.content
