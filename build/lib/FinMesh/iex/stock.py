from ._common import *
"""Should mostly use class from now on and use these functions as the 'backend'"""

#   Balance Sheet
IEX_BALANCE_SHEET_URL = prepend_iex_url('stock') + '{symbol}/balance-sheet'
def balance_sheet(symbol, vprint=False, **queries):
    """:return: Balance sheet financial statement for the requested stock.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param queries: Standard kwargs parameter.
    :type queries: key value pair where key is variable and value is string
    """
    # Returns balance sheet data for the requested ticker.
    url = replace_url_var(IEX_BALANCE_SHEET_URL, symbol=symbol)
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)


#   Batch Requests
def batch_requests():
    raise ImplementationError("Function cannot be implemented.")


#   Book
IEX_BOOK_URL = prepend_iex_url('stock') + '{symbol}/book?'
def book(symbol, vprint=False):
    """:return: Book price for the requested stock.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    # Returns book price data for the requested ticker.
    url = replace_url_var(IEX_BOOK_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Cash Flow
IEX_CASH_FLOW_URL = prepend_iex_url('stock') + '{symbol}/cash-flow'
def cash_flow(symbol, vprint=False, **queries):
    """:return: Cash sheet financial statment for the requested stock.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param queries: Standard kwargs parameter.
    :type queries: key value pair where key is variable and value is string
    """
    url = replace_url_var(IEX_CASH_FLOW_URL, symbol=symbol)
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)


#   Collections
IEX_COLLECTION_URL = prepend_iex_url('stock') + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName, vprint=False):
    """:return: Quotes for stock in the requested collection type.

    :param collectionType: The type of data returned by the endpoint.
    :type collectionType: accepted values are ['sector', 'tag', 'list'], required
    :param collectionName: Name of the sector, tag, or list to return. List of names available on IEX Cloud.
    :type collectionName: string, required
    """
    url = replace_url_var(IEX_COLLECTION_URL, collectionType=collectionType, collectionName=collectionName)
    return get_iex_json_request(url, vprint=vprint)


#   Company
IEX_COMPANY_URL = prepend_iex_url('stock') + '{symbol}/company?'
def company(symbol, vprint=False):
    """:return: Company data such as website, address, and description for the requested company.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_COMPANY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Delayed Quote
IEX_DELAYED_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/delayed-quote?'
def delayed_quote(symbol, vprint=False):
    """:return: 15-minute delayed market quote for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_DELAYED_QUOTE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Dividends
IEX_DIVIDENDS_URL = prepend_iex_url('stock') + '{symbol}/dividends/{scope}?'
def dividends(symbol, scope, vprint=False):
    """:return: Returns dividend information for a requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param scope: The range of data needed.
    :type scope: accepted arguments: ['5y','2y','1y','ytd','6m','3m','1m','next'], required
    """

    url = replace_url_var(IEX_DIVIDENDS_URL, symbol=symbol, scope=scope)
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
def estimates(symbol, vprint=False):
    """:return: Latest future earnings estimates for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_ESTIMATES_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Financials
IEX_FINANCIALS_URL = prepend_iex_url('stock') + '{symbol}/financials?'
def financials(symbol, period=None, vprint=False):
    """:return: Brief overview of a company's financial statements.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param period: The time interval of financial statements returned.
    :type period: accepted values are ['annual', 'quarterly'], optional
    """
    url = replace_url_var(IEX_FINANCIALS_URL, symbol=symbol)
    url += f'period={period}' if period else ''
    return get_iex_json_request(url, vprint=vprint)


#   Fund Ownership
IEX_FUND_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/fund-ownership?'
def fund_ownership(symbol, vprint=False):
    """:return: Largest 10 fund owners of the requested ticker. This excludes explicit buy or sell-side firms.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_FUND_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


IEX_HISTORICAL_URL = prepend_iex_url('stock')
def historical_price(symbol, period, date=None, vprint=False, **queries):
    """This is a mess and will soon be deprecated in favour of an args and kwargs based approach."""
    url = IEX_HISTORICAL_URL + f"{symbol}/chart/{period}"
    if period == 'date':
        url += f'/{date}?&chartByDay=True'
    else:
        url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    url = append_iex_token(url)
    if vprint: print(f"Now fetching: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

#   HISTORICAL PRICE
IEX_HISTORICAL_URL = prepend_iex_url('stock')
def new_historical_price(symbol, period, date=None, chartByDay=False, **query_string_params, vprint=False):
    """:return: Adjusted and unadjusted historical data for up to 15 years, and historical minute-by-minute intraday prices for the last 30 trailing calendar days.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param period: The period of data you would like to have returned.
    Accepted arguments are ['max', '5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1mm', '5d', '5dm', 'date', 'dynamic']
    :type period: string, required
    :param date: If used with the query parameter chartByDay, then this returns historical OHLCV data for that date. Otherwise, it returns data by minute for a specified date. Date format YYYYMMDD
    :type date: string, optional
    :param chartByDay: If single date is specified, this returns historical OHLCV data for that date.
    :type chartByDay: boolean, optional

    Query string parameters allow you to specify what data you want on a finer scale.
    Boolean parameters should be typed as strings in the following format: '``key=value``'

    A full list of these parameters can be found in the IEX documentation.
    """
    url = IEX_HISTORICAL_URL + f'{symbol}/chart/{period}'
    if chartByDay and period == 'date': url += f'{date}?chartByDay=True'
    else:
        url += '?'
        for key, value in query_string_params.items():
            url += f'{key}={value}?'
    url = append_iex_token(url)
    if vprint: print(f"Now fetching: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    return result


#   Income Statement
IEX_INCOME_STATEMENT_URL = prepend_iex_url('stock') + '{symbol}/income'
def income_statement(symbol, vprint=False, **queries):
    """:return: Income statement financial data for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param queries: Standard kwargs parameter.
    :type queries: key value pair where key is variable and value is string
    """
    url = replace_url_var(IEX_INCOME_STATEMENT_URL, symbol=symbol)
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)


#   Insider Roster
IEX_INSIDER_ROSTER_URL = prepend_iex_url('stock') + '{symbol}/insider-roster?'
def insider_roster(symbol, vprint=False):
    """:return: 10 largest insider owners for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_INSIDER_ROSTER_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Insider Summary
IEX_INSIDER_SUMMARY_URL = prepend_iex_url('stock') + '{symbol}/insider-summary?'
def insider_summary(symbol, vprint=False):
    """:return: Summary of the insiders and their actions within the last 6 months for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_INSIDER_SUMMARY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Insider Transactions
IEX_INSIDER_TRANSACTIONS_URL = prepend_iex_url('stock') + '{symbol}/insider-transactions?'
def insider_transactions(symbol, vprint=False):
    """:return: Summary of insider transactions for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_INSIDER_TRANSACTIONS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Institutional Ownership
IEX_INSTITUTIONAL_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/institutional-ownership?'
def institutional_ownership(symbol, vprint=False):
    """:return: 10 largest instituional owners for the requested ticker. This is defined as explicitly buy or sell-side only.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_INSTITUTIONAL_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   IPO Calendar
IEX_UPCOMING_IPOS_URL = prepend_iex_url('stock') + 'market/upcoming-ipos?'
def ipo_upcoming(vprint=False):
    """:return: List of upcoming IPOs for the current and next month."""
    return get_iex_json_request(IEX_UPCOMING_IPOS_URL)


IEX_TODAY_IPOS_URL = prepend_iex_url('stock') + 'market/today-ipos?'
def ipo_today(vprint=False):
    """:return: List of IPOs happening today."""
    return get_iex_json_request(IEX_TODAY_IPOS_URL)


#   Key Stats
IEX_STATS_URL = prepend_iex_url('stock') + '{symbol}/stats'
def key_stats(symbol, stat=False, vprint=False):
    """:return: Important and key statistics for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param stat: The specific stat which you would like to return.
    :type stat: string, optional
    """
    url = replace_url_var(IEX_STATS_URL, symbol=symbol)
    url += str(stat) if stat else '?'
    return get_iex_json_request(url, vprint=vprint)


#   Largest Trades
IEX_LARGEST_TRADES_URL = prepend_iex_url('stock') + '{symbol}/largest-trades?'
def largest_trades(symbol, vprint=False):
    """:return: Delayed list of largest trades for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_LARGEST_TRADES_URL, symbol=symbol)
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


#   Logo
IEX_LOGO_URL = prepend_iex_url('stock') + '{symbol}/logo?'
def logo(symbol, vprint=False):
    """:return: Google APIs link to the logo for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_LOGO_URL, symbol=symbol)
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


#   News
IEX_NEWS_URL = prepend_iex_url('stock') + '{symbol}/news'
def news(symbol, last=None, vprint=False):
    """:return: News item summaries for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param last: The number of news items to return.
    :type last: integer, optional
    """
    url = replace_url_var(IEX_NEWS_URL, symbol=symbol)
    url += f'/last/{last}?' if last else '?'
    return get_iex_json_request(url, vprint=vprint)


#   OHLC
IEX_OHLC_URL = prepend_iex_url('stock') + '{symbol}/ohlc?'
def ohlc(symbol, vprint=False):
    """:return: Most recent days open, high, low, and close data for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_OHLC_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Peers
IEX_PEERS_URL = prepend_iex_url('stock') + '{symbol}/peers?'
def peers(symbol, vprint=False):
    """:return: List of a requested ticker's peers.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_PEERS_URL, symbol=symbol)
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


#   Price
IEX_PRICE_URL = prepend_iex_url('stock') + '{symbol}/price?'
def price(symbol, vprint=False):
    """:return: Single float value of the requested ticker's price.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_PRICE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Price Target
IEX_PRICE_TARGET_URL = prepend_iex_url('stock') + '{symbol}/price-target?'
def price_target(symbol, vprint=False):
    """:return: Analyst's price targets for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_PRICE_TARGET_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Quote
IEX_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/quote'
def quote(symbol, field=None, vprint=False):
    """:return: rice quote data for the requested ticker. Fields are able to be called individually.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param field: The specific field from the quote endpoint you would like to return.
    :type field: string, optional
    """
    url = replace_url_var(IEX_QUOTE_URL, symbol=symbol)
    url += f'/{field}?' if field else '?'
    return get_iex_json_request(url, vprint=vprint)


#   Recommended Trends
IEX_RECOMMENDED_TRENDS_URL = prepend_iex_url('stock') + '{symbol}/recommendation-trends?'
def recommendation_trends(symbol, vprint=False):
    """:return: Analyst recommendations for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_RECOMMENDED_TRENDS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Sector Performance
IEX_SECTOR_PERFORMANCE_URL = prepend_iex_url('stock') + 'market/sector-performance?'
def sector_performance(vprint=False):
    """:return: Market performance for all sectors."""
    return get_iex_json_request(IEX_SECTOR_PERFORMANCE_URL)


#   Splits
IEX_SPLITS_URL = prepend_iex_url('stock') + '{symbol}/splits'
def splits(symbol, scope=None, vprint=False):
    """:return: Record of stock splits for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param scope: The range of data needed.
    :type scope: accepted arguments: ['5y','2y','1y','ytd','6m','3m','1m','next'], optional
    """
    url = replace_url_var(IEX_SPLITS_URL, symbol=symbol)
    url += f'/{scope}?' if scope else '?'
    return get_iex_json_request(url, vprint=vprint)


#   Volume by Venue
IEX_VOLUME_BY_VENUE_URL = prepend_iex_url('stock') + '{symbol}/volume-by-venue'
def volume_by_venue(symbol, vprint=False):
    """:return: rading volume for the requested ticker by venue.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    url = replace_url_var(IEX_VOLUME_BY_VENUE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
