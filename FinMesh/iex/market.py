from _common import *

IEX_DATA_POINT_URL = 'https://cloud.iexapis.com/stable/data-points/'
IEX_TIME_SERIES_URL = 'https://cloud.iexapis.com/stable/time-series/'

IEX_COMMODITIES_URL = IEX_DATA_POINT_URL + 'market/'
def commodities(symbol, vprint=False):
    ## Returns commodites data for the requested commodities symbol.
    url = IEX_COMMODITIES_URL + f'{symbol}?'
    return get_iex_json_request(url, vprint=vprint)
commodities.__doc__='Returns commodites data for the requested commodities symbol.'

IEX_ECONOMIC_URL = IEX_DATA_POINT_URL + 'market/'
def economic_data(symbol, vprint=False):
    ## Returns economic data for the requested economic indicator symbol.
    url = IEX_ECONOMIC_URL + f'{symbol}?'
    return get_iex_json_request(url, vprint=vprint)
economic_data.__doc__='Returns economic data for the requested economic indicator symbol.'

def generic_data_point(symbol, key, vprint=False, **queries):
    """Credit usage depends on what is requested.
    This is a generic endpoint for any and all data points available on IEX Cloud.
    Parameters:
    symbol -> the symbol for the datapoint you wish to retrieve
    key -> the classification for the datapoint you wish to retrieve
    **queries -> enter any key/value pairs into the arguments and they will be transferred to the request
    """
    url = IEX_DATA_POINT_URL + f'{key}/{symbol}?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)

def generic_time_series(symbol, key, vprint=False, **queries):
    """Credit usage depends on what is requested.
    This is a generic endpoint for any and all time series data available on IEX Cloud.
    Parameters:
    symbol -> the symbol for the time series you wish to retrieve
    key -> the classification for the time series you wish to retrieve
    **queries -> enter any key/value pairs into the arguments and they will be transferred to the request
    """
    url = IEX_TIME_SERIES_URL + f'{key}/{symbol}?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)

#   Collections
IEX_COLLECTION_URL = prepend_iex_url('stock') + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName, vprint=False):
    # Returns a list of tickers belonging to the requested collection.
    url = replace_url_var(IEX_COLLECTION_URL, collectionType=collectionType, collectionName=collectionName)
    return get_iex_json_request(url, vprint=vprint)
collection.__doc__='Returns quotes for stocks in the requested collection type.'
