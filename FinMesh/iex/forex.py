from ._common import *

# Latest Rates
FOREX_LATEST_URL = prepend_iex_url('fx') + 'latest?'
def forex_latest_rate(symbols, vprint=False):
    """Returns the latest exchange rate for the requested currency pair.
    """
    url = FOREX_LATEST_URL + f'symbols={symbols}'
    return get_iex_json_request(url, vprint=vprint)


# Currency Conversion
FOREX_CONVERSION_URL = prepend_iex_url('fx') + 'convert?'
def forex_conversion(symbols, amount, vprint=False):
    """Returns a converted value according to the requested currency pair.
    """
    url = FOREX_CONVERSION_URL + f'symbols={symbols}&amount={amount}'
    return get_iex_json_request(url, vprint=vprint)


# Historical Data
FOREX_HISTORICAL_URL = prepend_iex_url('fx') + 'historical?'
def forex_historical(symbols, vprint=False, **queries):
    """Returns a list of the historical exchange rates for the requested currency pair.
    """
    url = FOREX_HISTORICAL_URL + f'symbols={symbols}'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    url =+ '&'
    return get_iex_json_request(url, vprint=vprint)
