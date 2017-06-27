import requests

def is_up(url):
    return requests.get(url).status_code == 200


