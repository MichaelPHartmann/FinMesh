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
def fred_series(series, file_type=None, realtime_start=None, realtime_end=None, limit=None, offset=None, sort_order=None, observation_start=None, observation_end=None, units=None, frequency=None, aggregation_method=None, output_type=None, vintage_dates=None):
    ## Returns time series historical data for the requested FRED data.
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
fred_series.__doc__='Returns time series historical data for the requested FRED data.'

GEOFRED_SERIES_META_URL = GEOFRED_BASE_URL + 'series/group?'
def geofred_series_meta(series_id, file_type=None):
    ## Returns meta data for the requested FRED data.
    url = GEOFRED_SERIES_META_URL + f'series_id={series_id}'
    if file_type: url += f'&file_type={file_type}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text
geofred_series_meta.__doc__='Returns meta data for the requested FRED data.'

GEOFRED_REGIONAL_SERIES_URL = GEOFRED_BASE_URL + 'series/data?'
def geofred_regional_series(series_id, file_type=None, date=None, start_date=None):
    ## Returns the historical, geographically organized time series data for the requested FRED data.
    url = GEOFRED_REGIONAL_SERIES_URL + f'series_id={series_id}'
    if file_type: url += f'&file_type={file_type}'
    if date: url += f'&date={date}'
    if start_date: url += f'&start_date={start_date}'
    url = append_fred_token(url)
    result = requests.get(url)
    return result.text
geofred_regional_series.__doc__='Returns the historical, geographically organized time series data for the requested FRED data.'

# # # # # # # # # # # # # # # #
# GOVERNMENT YIELD CURVE DATA #
# # # # # # # # # # # # # # # #

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%204%20and%20year(NEW_DATE)%20eq%202019'

def get_yield():
    ## Returns government treasury bond yields. Organized in Python dictionary format by bond length.

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
get_yield.__doc__='Returns government treasury bond yields. Organized in Python dictionary format by bond length.'
