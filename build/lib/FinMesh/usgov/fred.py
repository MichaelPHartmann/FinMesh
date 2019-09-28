import os
import csv
import json
import requests
import xmltodict


FRED_BASE_URL = 'https://api.stlouisfed.org/fred/'
GEOFRED_BASE_URL = 'https://api.stlouisfed.org/geofred/'

def append_fred_token(url):
    token = os.getenv('FRED_TOKEN')
    return f'{url}&api_key={token}'

FRED_SERIES_OBS_URL = FRED_BASE_URL + 'series/observations?'
def fred_series(series, file_type=None, realtime_start=None, realtime_end=None, limit=None, offset=None, sort_order=None, observation_start=None, observation_end=None, units=None, frequency=None, aggregation_method=None, output_type=None, vintage_dates=None):
    url = FRED_SERIES_OBS_URL + f'series_id={series}'
    if file_type: url += f'&file_type={file_type}'
    if realtime_start: url += f'&realtime_start={realtime_start}'
    if realtime_end: url += f'&realtime_end={realtime_end}'
    if limit: url += f'&limit={limit}'
    if offset: url += f'&offset={offset}'
    if sort_order: url += f'&sort_order={sort_order}'
    if observation_start: url += f'&observation_start={observation_start}'
    if observation_end: url += f'&observation_end={observation_end}'
    if units: url += f'&units={units}'
    if frequency: url += f'&frequency={frequency}'
    if aggregation_method: url += f'&aggregation_method={aggregation_method}'
    if output_type: url += f'&output_type={output_type}'
    if vintage_dates: url += f'&vintage_dates={vintage_dates}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text

GEOFRED_SERIES_META_URL = GEOFRED_BASE_URL + 'series/group?'
def geofred_series_meta(series_id, file_type=None):
    url = GEOFRED_SERIES_META_URL + f'series_id={series_id}'
    if file_type: url += f'&file_type={file_type}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text

GEOFRED_REGIONAL_SERIES_URL = GEOFRED_BASE_URL + 'series/data?'
def geofred_regional_series(series_id, file_type=None, date=None, start_date=None):
    url = GEOFRED_REGIONAL_SERIES_URL + f'series_id={series_id}'
    if file_type: url += f'&file_type={file_type}'
    if date: url += f'&date={date}'
    if start_date: url += f'&start_date={start_date}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text
