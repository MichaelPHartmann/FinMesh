from ._common import *

#   Price Target
IEX_PRICE_TARGET_URL = prepend_iex_url('stock') + '{symbol}/price-target?'
def price_target(symbol, vprint=False):
    """:return: Analyst's price targets for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_PRICE_TARGET_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Earnings
IEX_EARNINGS_URL = prepend_iex_url('stock') + '{symbol}/earnings'
def earnings(symbol, last=None, field=None, vprint=False):
    """:return: Earnings data such as actual EPS, beat/miss, and date for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param last: The number of previous earnings to return.
    :type last: string, optional
    :param field: The specific field from the earnings report ot return.
    :type field: string, optional
    """
    url = replace_url_var(IEX_EARNINGS_URL, symbol=symbol)
    if last and field:
        url+= f"/{last}/{field}?"
    elif last:
        url+= f"/{last}?"
    else:
        url += '?'
    return get_iex_json_request(url, vprint=vprint)


#   Earnings Today
IEX_TODAY_EARNINGS_URL = prepend_iex_url('stock') + 'market/today-earnings?'
def today_earnings(vprint=False):
    """:return: Earnings data released today, grouped by timing and stock."""
    url = IEX_TODAY_EARNINGS_URL
    return get_iex_json_request(url, vprint=vprint)


#   Estimates
IEX_ESTIMATES_URL = prepend_iex_url('stock') + '{symbol}/estimates?'
def future_estimates(symbol, vprint=False):
    """:return: Latest future earnings estimates for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_ESTIMATES_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   List
IEX_MARKET_LIST_URL = prepend_iex_url('stock') + '{symbol}/list/{list_type}?'
def market_list(list_type, displayPercent=None, vprint=False):
    """:return: 10 largest companies in the specified list.

    :param list_type: The list that you would like to return.
    :type list_type: accepted values are ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent', 'premarket_losers', 'postmarket_losers', 'premarket_gainers', 'postmarket_gainers'], required
    :param displayPercent: Whether you would like to see the percentage values multiplied by 100
    :type displayPercent: boolean, optional
    """
    url = replace_url_var(IEX_MARKET_LIST_URL, symbol=symbol, list_type=list_type)
    url += f'displayPercent={displayPercent}' if displayPercent else ''
    return get_iex_json_request(url, vprint=vprint)


#   Market Volume (U.S.)
IEX_MARKET_VOLUME_URL = prepend_iex_url('stock') + 'market/volume?'
def market_volume(format=None, vprint=False):
    """:return: Market wide trading volume.

    :param format: The output format of the endpoint
    :type format: accepted value is 'csv', optional
    """
    url = IEX_MARKET_VOLUME_URL
    url += f'format={format}' if format else ''
    return get_iex_json_request(url, vprint=vprint)


#   Previous Day Prices
IEX_PREVIOUS_URL = prepend_iex_url('stock') + '{symbol}/previous?'
def previous(symbol, vprint=False):
    """:return: Previous day's price data for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_PREVIOUS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Recommended Trends
IEX_RECOMMENDED_TRENDS_URL = prepend_iex_url('stock') + '{symbol}/recommendation-trends?'
def recommendation_trends(symbol, vprint=False):
    """:return: analyst recommendations for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_RECOMMENDED_TRENDS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
