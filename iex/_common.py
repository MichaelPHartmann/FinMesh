import os
import requests

def append_iex_token(url):
    token = os.getenv('IEX_TOKEN')
    return f"{url}&token={token}"

def get_iex_json_request(url, vprint=False):
    url = append_iex_token(url)
    if vprint: print(f"Making request: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

def replace_url_var(url, **kwargs):
    for key, value in kwargs.items():
        url = url.replace('{' + key + '}', value)
    return url
