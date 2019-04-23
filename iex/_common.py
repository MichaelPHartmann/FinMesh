import requests
import os

VERBOSE = True # Turn on explanitory output

def vprint(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)

def append_iex_token(url):
    token = os.getenv('IEX_TOKEN')
    return f"{url}&token={token}"

def get_iex_json_request(url):
    url = append_iex_token(url)
    vprint(f"Making request: {url}")
    result = requests.get(url)
    vprint(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

def replace_url_var(url, **kwargs):
    for key, value in kwargs.items():
        url = url.replace('{' + key + '}', value)
    return url
