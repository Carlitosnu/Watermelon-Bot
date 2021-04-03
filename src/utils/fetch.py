import requests


def get(url):
    r = requests.get(url)
    if r.status_code == 200:
        return [r.status_code, r.json()]
    else:
        return [r.status_code]


def getWithHeaders(url, headers):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return [r.status_code, r.json()]
    else:
        return [r.status_code]
