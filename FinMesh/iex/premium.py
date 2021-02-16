from ._common import *

#   Earnings
IEX_EARNINGS_URL = prepend_iex_url('stock') + '{symbol}/earnings'
def earnings(symbol, last=None, field=None, vprint=False):
    # Returns earnings data such as actual EPS, beat/miss, and date for the requested ticker.
    url = replace_url_var(IEX_EARNINGS_URL, symbol=symbol)
    if last and field:
        url+= f"/{last}/{field}?"
    elif last:
        url+= f"/{last}?"
    else:
        url += '?'
    return get_iex_json_request(url, vprint=vprint)
earnings.__doc__='Returns earnings data such as actual EPS, beat/miss, and date for the requested stock. Requires premium credits to access.'
