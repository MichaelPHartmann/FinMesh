import os
import json
import requests
import xmltodict

FRED_BASE_URL = 'https://api.stlouisfed.org/fred/'

def append_fred_token(url):
    token = os.getenv('FRED_TOKEN')
    return f'{url}&api_key={token}'

SERIES_OBS_URL = FRED_BASE_URL + 'series/observations?'
def fred_series(series, file_type):
    url = SERIES_OBS_URL + f'series_id={series}&file_type={file_type}'
    url = append_fred_token(url)
    result = requests.get(url)
    if file_type == 'json':
        result = result.json()
    elif file_type == 'xml':
        result = xmltodict.parse(result.content)
    return result

print(fred_series('GNPCA', 'json'))
