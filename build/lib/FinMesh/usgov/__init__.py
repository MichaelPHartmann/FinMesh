import os
import requests
import xmltodict
import csv
import json

# # # # # # # # # #
# FRED DATA BELOW #
# # # # # # # # # #

FRED_BASE_URL = 'https://api.stlouisfed.org/fred/'
GEOFRED_BASE_URL = 'https://api.stlouisfed.org/geofred/'

def append_fred_token(url):
    token = os.getenv('FRED_TOKEN')
    return f'{url}&api_key={token}'

FRED_SERIES_OBS_URL = FRED_BASE_URL + 'series/observations?'
def fred_series(series_id, **queries):
    """Returns time series historical data for the requested FRED data.
    Parameters:
    series_id -> The only required parameter. The id for the data series you wish to access.
    queries -> Accepts key-value pairs for the various parameters available on FRED. (file_type, date, offset, etc.)
    """
    url = FRED_SERIES_OBS_URL + f'series_id={series}'
    for key, value in queries.items():
        url += f'&{key}={value}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text


GEOFRED_SERIES_META_URL = GEOFRED_BASE_URL + 'series/group?'
def geofred_series_meta(series_id, file_type=None):
    """Returns meta data for the requested FRED data."""
    url = GEOFRED_SERIES_META_URL + f'series_id={series_id}'
    if file_type: url += f'&file_type={file_type}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text


GEOFRED_REGIONAL_SERIES_URL = GEOFRED_BASE_URL + 'series/data?'
def geofred_regional_series(series_id, **queries):
    """Returns the historical, geographically organized time series data for the requested FRED data.
    Parameters:
    series_id -> The only required parameter. The id for the data series you wish to access.
    queries -> accepts key-value pairs for the various parameters available on FRED. (file_type, date, etc.)
    """
    url = GEOFRED_REGIONAL_SERIES_URL + f'series_id={series_id}'
    for key, value in queries.items():
        url += f'&{key}={value}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text

# # # # # # # # # # # # # # # #
# GOVERNMENT YIELD CURVE DATA #
# # # # # # # # # # # # # # # #

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%204%20and%20year(NEW_DATE)%20eq%202019'

def get_yield():
    """Returns government treasury bond yields. Organized in Python dictionary format by bond length."""

    # Formatting of XML to Python Dict
    curve = requests.get(GOV_YIELD_URL)
    parse_curve = xmltodict.parse(curve.content)

    # This is based around retrieving the n last dates or average of n days.
    feed = parse_curve['feed']
    entry = feed['entry']
    last_entry = len(entry)-1
    content = entry[last_entry]['content']['m:properties']

    # Dict that contains the whole yield curve so there is no need to bring in each rate.
    yield_curve_values = {
        'date' : entry[last_entry]['content']['m:properties']['d:NEW_DATE']['#text'],
        '1month' : float(content['d:BC_1MONTH']['#text']),
        '2month' : float(content['d:BC_2MONTH']['#text']),
        '3month' : float(content['d:BC_3MONTH']['#text']),
        '6month' : float(content['d:BC_6MONTH']['#text']),
        '1year' : float(content['d:BC_1YEAR']['#text']),
        '2year' : float(content['d:BC_2YEAR']['#text']),
        '3year' : float(content['d:BC_3YEAR']['#text']),
        '5year' : float(content['d:BC_5YEAR']['#text']),
        '10year' : float(content['d:BC_10YEAR']['#text']),
        '20year' : float(content['d:BC_20YEAR']['#text']),
        '30year' : float(content['d:BC_30YEAR']['#text']),
        }
    return yield_curve_values
