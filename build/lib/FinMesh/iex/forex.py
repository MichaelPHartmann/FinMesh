from ._common import *
"""Should mostly use class from now on and use these functions as the 'backend'"""

# Latest Rates
FOREX_LATEST_URL = prepend_iex_url('fx') + 'latest?'
def forex_latest_rate(symbols, vprint=False):
    """:return: Latest FOREX rate for the requested currency pair symbol.

    :param symbol: The symbol of the currency pair you would like to return.
    :type symbol: string, required
    """
    url = FOREX_LATEST_URL + f'symbols={symbols}'
    return get_iex_json_request(url, vprint=vprint)


# Currency Conversion
FOREX_CONVERSION_URL = prepend_iex_url('fx') + 'convert?'
def forex_conversion(symbols, amount, vprint=False):
    """:return: Converts one currency to another using up-to-date currency information.

    :param symbol: The symbol of the currency pair you would like to return.
    :type symbol: string, required
    :param amount: The amount of the primary currency you wish to calculate and exchange rate on.
    :type amount: float, required
    """
    url = FOREX_CONVERSION_URL + f'symbols={symbols}&amount={amount}'
    return get_iex_json_request(url, vprint=vprint)


# Historical Data
FOREX_HISTORICAL_URL = prepend_iex_url('fx') + 'historical?'
def forex_historical(symbols, vprint=False, **queries):
    """:return: Historical FOREX rates for the requested currency pair symbol.

    :param symbol: The symbol of the currency pair you would like to return.
    :type symbol: string, required
    """
    url = FOREX_HISTORICAL_URL + f'symbols={symbols}'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    url =+ '&'
    return get_iex_json_request(url, vprint=vprint)
