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

def append_fred_token(url, external=None):
    if external:
        token = external
    else:
        token = os.getenv('FRED_TOKEN')
    return f'{url}&api_key={token}'

FRED_SERIES_OBS_URL = FRED_BASE_URL + 'series/observations?'
def fred_series(series, external=None, **query_params):
    """ Returns series data from the US Federal Reserve and Economic Database (FRED) API.

    :param series: The series ID of the data you want to return.
    :type series: string, required
    :param external: If you want to use a token from outside your environment variables, use this param
    :type external: string, optional, default None
    :param file_type:
    :type file_type: string, optional
    :param realtime_start:
    :type realtime_start: string, optional
    :param realtime_end:
    :type realtime_end: string, optional
    :param limit:
    :type limit: string, optional
    :param offset:
    :type offset: string, optional
    :param sort_order:
    :type sort_order: string, optional
    :param observation_start:
    :type observation_start: string, optional
    :param observation_end:
    :type observation_end: string, optional
    :param units:
    :type units: string, optional
    :param frequency:
    :type frequency: string, optional
    :param aggregation_method:
    :type aggregation_method: string, optional
    :param output_type:
    :type output_type: string, optional
    :param vintage_dates:
    :type vintage_dates: string, optional

    :return: Returns time series historical data for the requested FRED data
    """
    url = FRED_SERIES_OBS_URL + f'series_id={series}'
    for key, value in query_params.items():
        url += F'&{key}={value}'
    url = append_fred_token(url, external=external)
    result = requests.get(url)
    return result.text


GEOFRED_SERIES_META_URL = GEOFRED_BASE_URL + 'series/group?'
def geofred_series_meta(series, external=None, **query_params):
    """Returns series meta data from the US Federal Reserve and Economic Database (FRED) API.

    :param series: The series ID of the data you want to return.
    :type series: string, required
    :param external: If you want to use a token from outside your environment variables, use this param
    :type external: string, optional, default None

    :return: Returns meta data for the requested FRED data
    """
    url = GEOFRED_SERIES_META_URL + f'series_id={series}'
    for key, value in query_params.items():
        url += F'&{key}={value}'
    url = append_fred_token(url, external=external)
    result = requests.get(url)
    if result.ok:
        return result.text
    else:
        return (F"There was an error with the request to IEX!\n"
                + F"{response.status_code}:{response.reason} in {round(response.elapsed.microseconds/1000000,4)} seconds\n"
                + F"URL: {response.url}\n"
                + "Response Content:\n"
                + F"{response.text}")


GEOFRED_REGIONAL_SERIES_URL = GEOFRED_BASE_URL + 'series/data?'
def geofred_regional_series(series, external=None, **query_params):
    """Returns geographically organized series data from the US Federal Reserve and Economic Database (FRED) API.

    :param series: The series ID of the data you want to return.
    :type series: string, required
    :param external: If you want to use a token from outside your environment variables, use this param
    :type external: string, optional, default None
    :param query_params: This function accepts any and all key-value pairs, but does not guarantee the validity of their use
    :type query_params: strings, key-value pairs, optional

    :return: Returns the historical, geographically organized time series data for the requested FRED data
    """
    url = GEOFRED_REGIONAL_SERIES_URL + f'series_id={series}'
    for key, value in query_params.items():
        url += F'&{key}={value}'
    url = append_fred_token(url, external=external)
    result = requests.get(url)
    if result.ok:
        return result.text
    else:
        return (F"There was an error with the request to IEX!\n"
                + F"{response.status_code}:{response.reason} in {round(response.elapsed.microseconds/1000000,4)} seconds\n"
                + F"URL: {response.url}\n"
                + "Response Content:\n"
                + F"{response.text}")


# # # # # # # # # # # # # # # #
# GOVERNMENT YIELD CURVE DATA #
# # # # # # # # # # # # # # # #

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%204%20and%20year(NEW_DATE)%20eq%202019'
def get_yield():
    """A function that retrieves current Treasury Bond rates from the US Treasury website.
    :return: Dictionary containing all the T-Bond terms as keys (strings) and their rates as values (floats).
    """

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
