import os
import requests

# Simple string comprehension to allow setting of states through environment variables.
def arg_to_bool(string):
    affirmative = ['True','TRUE','true','Yes','YES','yes','On','ON','on']
    if string in affirmative:
        return True
    else:
        return False

def prepend_iex_url(section):
    sandboxState = arg_to_bool(os.getenv('SANDBOX'))
    if sandboxState is True:
        url = f'https://sandbox.iexapis.com/stable/{section}/'
    else:
        url = f'https://cloud.iexapis.com/stable/{section}/'
    return url

def append_iex_token(url, external=False):
    sandboxState = arg_to_bool(os.getenv('SANDBOX'))
    if external is True:
        pass
    else:
        if sandboxState is True:
            token = os.getenv('IEX_SANDBOX_TOKEN')
        else:
            token = os.getenv('IEX_TOKEN')
        return f"{url}&token={token}"

def get_iex_json_request(url, external=False, vprint=False):
    url = append_iex_token(url, external=external)
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
