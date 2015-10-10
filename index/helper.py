import requests

def get_request(url):
    r = requests.get(url)
    return r.content

def post_request(url, payload):
    r = requests.post(url, data=payload)
    return r.content
