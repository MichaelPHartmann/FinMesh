from ._common import *
"""Should mostly use class from now on and use these functions as the 'backend'"""

IEX_DATA_POINT_URL = 'https://cloud.iexapis.com/stable/data-points/'
IEX_TIME_SERIES_URL = 'https://cloud.iexapis.com/stable/time-series/'

IEX_COMMODITIES_URL = IEX_DATA_POINT_URL + 'market/'
def commodities(symbol, vprint=False):
    """:return: Commodites data for the requested commodities symbol.

    :param symbol: The symbol of the commodity you would like to return.
    :type symbol: string, required
    """
    url = IEX_COMMODITIES_URL + f'{symbol}?'
    return get_iex_json_request(url, vprint=vprint)


IEX_ECONOMIC_URL = IEX_DATA_POINT_URL + 'market/'
def economic_data(symbol, vprint=False):
    """:return: Economic data for the requested economic indicator symbol.

    :param symbol: The symbol of the economic indicator you would like to return.
    :type symbol: string, required
    """
    url = IEX_ECONOMIC_URL + f'{symbol}?'
    return get_iex_json_request(url, vprint=vprint)


IEX_DATA_POINT_URL = 'https://cloud.iexapis.com/stable/data-points/'
def generic_data_point(symbol, key=None, vprint=False):
    """:return: Generic endpoint used to access all 'Data Point' data sets on IEX

    :param symbol: The symbol of the data point you would like to return.
    :type symbol: string, required
    """
    url = IEX_DATA_POINT_URL + f'{symbol}'
    if key:
        url += f'/{key}?'
    else:
        url+= '?'
    return get_iex_json_request(url, vprint=vprint)


IEX_TIME_SERIES_URL = 'https://cloud.iexapis.com/stable/time-series/'
def generic_time_series(symbol, *args, vprint=False):
    ## Generic endpoint used to access all 'Time Series' data sets on IEX
    """:return: Generic endpoint used to access all 'Time Series' data sets on IEX

    :param symbol: The symbol of the time series data you would like to return.
    :type symbol: string, required
    """
    url = IEX_TIME_SERIES_URL + f'{symbol}'
    for a in args:
        url += f'/{a}'
    url += '?'
    return get_iex_json_request(url, vprint=vprint)
