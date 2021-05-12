from ._common import *
"""Should mostly use class from now on and use these functions as the 'backend'"""

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
