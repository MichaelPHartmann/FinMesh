from ._common import *

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

IEX_DATA_POINT_URL = 'https://cloud.iexapis.com/stable/data-points/'
def generic_data_point(symbol, key=None, vprint=False):
    ## Generic endpoint used to access all 'Data Point' data sets on IEX
    url = IEX_DATA_POINT_URL + f'{symbol}'
    if key:
        url += f'/{key}?'
    else:
        url+= '?'
    return get_iex_json_request(url, vprint=vprint)
generic_data_point.__doc__='Generic endpoint used to access all \'Data Point\' data sets on IEX.'


IEX_TIME_SERIES_URL = 'https://cloud.iexapis.com/stable/time-series/'
def generic_time_series(symbol, *args, vprint=False):
    ## Generic endpoint used to access all 'Time Series' data sets on IEX
    url = IEX_TIME_SERIES_URL + f'{symbol}'
    for a in args:
        url += f'/{a}'
    url += '?'
    return get_iex_json_request(url, vprint=vprint)
generic_time_series.__doc__='Generic endpoint used to access all \'Time Series\' data sets on IEX'

#   Collections
IEX_COLLECTION_URL = prepend_iex_url('stock') + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName, vprint=False):
    # Returns a list of tickers belonging to the requested collection.
    url = replace_url_var(IEX_COLLECTION_URL, collectionType=collectionType, collectionName=collectionName)
    return get_iex_json_request(url, vprint=vprint)
collection.__doc__='Returns quotes for stocks in the requested collection type. May be deprecated.'
