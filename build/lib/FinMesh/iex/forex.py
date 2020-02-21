from ._common import *

# Latest Rates
FOREX_LATEST_URL = prepend_iex_url('fx') + 'latest?'
def forex_latest_rate(symbols, verbose=False):
    url = FOREX_LATEST_URL + f'symbols={symbols}'
    if verbose: print(url)
    return get_iex_json_request(url)

# Currency Conversion
FOREX_CONVERSION_URL = prepend_iex_url('fx') + 'convert?'
def forex_conversion(symbols, amount, verbose=False):
    url = FOREX_CONVERSION_URL + f'symbols={symbols}&amount={amount}'
    if verbose: print(url)
    return get_iex_json_request(url)

# Historical Data
FOREX_HISTORICAL_URL = prepend_iex_url('fx') + 'historical?'
def forex_historical(symbols, from=None, to=None, on=None, last=None, first=None, filter=None, format=None):
    url = FOREX_HISTORICAL_URL f'symbols={symbols}'
    if from: url =+ f'&from={from}'
    if to: url =+ f'&to={to}'
    if on: url =+ f'&on={on}'
    if last: url =+ f'&last={last}'
    if first: url =+ f'&first={first}'
    if filter: url =+ f'&filter={filter}'
    if format: url =+ f'&format={format}'
    url =+ '&'
    return get_iex_json_request(url)
