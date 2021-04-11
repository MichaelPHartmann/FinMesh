from ._common import *

#   Price Target
IEX_PRICE_TARGET_URL = prepend_iex_url('stock') + '{symbol}/price-target?'
def price_target(symbol, vprint=False):
    # Returns analyst's price targets for the requested ticker.
    url = replace_url_var(IEX_PRICE_TARGET_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
price_target.__doc__='Returns analyst\'s price targets for the requested stock.'

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

#   Earnings Today
IEX_TODAY_EARNINGS_URL = prepend_iex_url('stock') + 'market/today-earnings?'
def today_earnings(vprint=False):
    # Returns earnings data released today, grouped by timing and stock.
    url = IEX_TODAY_EARNINGS_URL
    return get_iex_json_request(url, vprint=vprint)
today_earnings.__doc__='Returns earnings data released today, grouped by timing and stock. Requires premium credits to access.'

#   Estimates
IEX_ESTIMATES_URL = prepend_iex_url('stock') + '{symbol}/estimates?'
def estimates(symbol, vprint=False):
    # Returns latest future earnings estimates for the requested ticker.
    url = replace_url_var(IEX_ESTIMATES_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
estimates.__doc__='Returns latest future earnings estimates for the requested stock. Requires premium credits to access.'

#   List
IEX_MARKET_LIST_URL = prepend_iex_url('stock') + '{symbol}/list/{list_type}?'
def market_list(symbol, list_type, displayPercent=None, vprint=False):
    # Returns the 10 largest companies in the specified list.
    url = replace_url_var(IEX_MARKET_LIST_URL, symbol=symbol, list_type=list_type)
    url += f'displayPercent={displayPercent}' if displayPercent else ''
    return get_iex_json_request(url, vprint=vprint)
market_list.__doc__='Returns the 10 largest companies in the specified list. May be deprecated or require premium credits to access.'

#   Market Volume (U.S.)
IEX_MARKET_VOLUME_URL = prepend_iex_url('stock') + 'market/volume?'
def market_volume(format=None, vprint=False):
    # Returns market wide trading volume.
    url = IEX_MARKET_VOLUME_URL
    url += f'format={format}' if format else ''
    return get_iex_json_request(url, vprint=vprint)
market_volume.__doc__='Returns market wide trading volume. Requires premium credits to access.'

#   Previous Day Prices
IEX_PREVIOUS_URL = prepend_iex_url('stock') + '{symbol}/previous?'
def previous(symbol, vprint=False):
    # Returns the previous day\'s price data for the requested ticker.
    url = replace_url_var(IEX_PREVIOUS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
previous.__doc__='Returns the previous day\'s price data for the requested stock. Requires premium credits to access.'

#   Recommended Trends
IEX_RECOMMENDED_TRENDS_URL = prepend_iex_url('stock') + '{symbol}/recommendation-trends?'
def recommendation_trends(symbol, vprint=False):
    # Returns analyst recommendations for the requested ticker.
    url = replace_url_var(IEX_RECOMMENDED_TRENDS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
recommendation_trends.__doc__='Returns analyst recommendations for the requested stocks. Requires premium credits to access.'
