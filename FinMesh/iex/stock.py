from ._common import *
"""Should mostly use class from now on and use these functions as the 'backend'"""\


def generic_iex_request(section, symbol, endpoint, append_subdirectory_to_url=None, external=False, **query_params):
    instance  = iexCommon(section, symbol, endpoint, external = external)
    if not append_subdirectory_to_url == None:
        instance.append_subdirectory_to_url(append_subdirectory_to_url)
    if not query_params == None:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

#   Balance Sheet
IEX_BALANCE_SHEET_URL = prepend_iex_url('stock') + '{symbol}/balance-sheet'
def balance_sheet(symbol, external=False, vprint=False, **query_params):
    """:return: Balance sheet financial statement for the requested stock.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param queries: Standard kwargs parameter.
    :type queries: key value pair where key is variable and value is string
    """
    instance = iexCommon('stock', symbol, 'balance-sheet', external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


#   Batch Requests
def batch_requests():
    raise ImplementationError("Function cannot be implemented.")


#   Book
IEX_BOOK_URL = prepend_iex_url('stock') + '{symbol}/book?'
def book(symbol, external=False, vprint=False):
    """:return: Book price for the requested stock.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'book', external=external)
    return instance.execute()


#   Cash Flow
IEX_CASH_FLOW_URL = prepend_iex_url('stock') + '{symbol}/cash-flow'
def cash_flow(symbol, external=False, vprint=False, **query_params):
    """:return: Cash sheet financial statment for the requested stock.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param queries: Standard kwargs parameter.
    :type queries: key value pair where key is variable and value is string
    """
    instance = iexCommon('stock', symbol, 'cash-flow', external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


#   Collections
IEX_COLLECTION_URL = prepend_iex_url('stock') + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName, external=False, vprint=False):
    """:return: Quotes for stock in the requested collection type.

    :param collectionType: The type of data returned by the endpoint.
    :type collectionType: accepted values are ['sector', 'tag', 'list'], required
    :param collectionName: Name of the sector, tag, or list to return. List of names available on IEX Cloud.
    :type collectionName: string, required
    """
    instance = iexCommon('stock', symbol, 'collection', external=external)
    instance.append_subdirectory_to_url(collectionType)
    query_params = {'collectionName' : collectionName}
    instance.append_query_params_to_url(query_params)
    return instance.execute()


#   Company
IEX_COMPANY_URL = prepend_iex_url('stock') + '{symbol}/company?'
def company(symbol, external=False, vprint=False, **query_params):
    """:return: Company data such as website, address, and description for the requested company.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'company', external=external)
    return instance.execute()


#   Delayed Quote
IEX_DELAYED_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/delayed-quote?'
def delayed_quote(symbol, external=False, vprint=False):
    """:return: 15-minute delayed market quote for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'delayed-quote', external=external)
    return instance.execute()


#   Dividends
IEX_DIVIDENDS_URL = prepend_iex_url('stock') + '{symbol}/dividends/{scope}?'
def dividends(symbol, scope, external=False, vprint=False):
    """:return: Returns dividend information for a requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param scope: The range of data needed.
    :type scope: accepted arguments: ['5y','2y','1y','ytd','6m','3m','1m','next'], required
    """
    instance = iexCommon('stock', symbol, 'dividends', external=external)
    instance.append_subdirectory_to_url(scope)
    return instance.execute()


#   Earnings
IEX_EARNINGS_URL = prepend_iex_url('stock') + '{symbol}/earnings'
def earnings(symbol, last=None, field=None, external=False, vprint=False):
    """:return: Earnings data such as actual EPS, beat/miss, and date for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param last: The number of previous earnings to return.
    :type last: string, optional
    :param field: The specific field from the earnings report ot return.
    :type field: string, optional
    """
    instance = iexCommon('stock', symbol, 'earnings', external=external)
    if last:
        instance.append_subdirectory_to_url(last)
        if field:
            instance.append_subdirectory_to_url(field)
    return instance.execute()


#   Earnings Today
IEX_TODAY_EARNINGS_URL = prepend_iex_url('stock') + 'market/today-earnings?'
def today_earnings(external=False, vprint=False):
    """:return: Earnings data released today, grouped by timing and stock."""
    return iexCommon('stock', 'market', 'today-earnings').execute()


#   Estimates
IEX_ESTIMATES_URL = prepend_iex_url('stock') + '{symbol}/estimates?'
def estimates(symbol, external=False, vprint=False):
    """:return: Latest future earnings estimates for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'estimates', external=external)
    return instance.execute()


#   Financials
IEX_FINANCIALS_URL = prepend_iex_url('stock') + '{symbol}/financials?'
def financials(symbol, period=None, external=False, vprint=False):
    """:return: Brief overview of a company's financial statements.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param period: The time interval of financial statements returned.
    :type period: accepted values are ['annual', 'quarterly'], optional
    """
    instance = iexCommon('stock', symbol, 'financials', external=external)
    if period:
        instance.append_query_params_to_url({'period' : period})
    return instance.execute()


#   Fund Ownership
IEX_FUND_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/fund-ownership?'
def fund_ownership(symbol, external=False, vprint=False):
    """:return: Largest 10 fund owners of the requested ticker. This excludes explicit buy or sell-side firms.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'fund-ownership', external=external)
    return instance.execute()


IEX_HISTORICAL_URL = prepend_iex_url('stock')
def historical_price(symbol, period, date=None, external=False, vprint=False, **query_params):
    """:return: Adjusted and unadjusted historical data for up to 15 years, and historical minute-by-minute intraday prices for the last 30 trailing calendar days.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param period: The period of data you would like to have returned.
    Accepted arguments are ['max', '5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1mm', '5d', '5dm', 'date', 'dynamic']
    :type period: string, required
    """
    instance = iexCommon('stock', symbol, 'chart', external=external)
    instance.append_subdirectory_to_url(period)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

#   HISTORICAL PRICE
IEX_HISTORICAL_URL = prepend_iex_url('stock')
def new_historical_price(symbol, period, date=None, chartByDay=False, external=False, vprint=False, **query_string_params):
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
    url = IEX_HISTORICAL_URL + f'{symbol}/chart/{period}/'
    if period == 'date':
        url += f'{date}'
        if chartByDay is True:
            url += '?chartByDay=true'
        else:
            url += '?chartByDay=false'

    for key, value in query_string_params.items():
        url += f'&{key}={value}'

    url = append_iex_token(url)
    if vprint: print(f"Now fetching: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    return result


#   Income Statement
IEX_INCOME_STATEMENT_URL = prepend_iex_url('stock') + '{symbol}/income'
def income_statement(symbol, external=False, vprint=False, **query_params):
    """:return: Income statement financial data for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param queries: Standard kwargs parameter.
    :type queries: key value pair where key is variable and value is string
    """
    instance = iexCommon('stock', symbol, 'income', external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


#   Insider Roster
IEX_INSIDER_ROSTER_URL = prepend_iex_url('stock') + '{symbol}/insider-roster?'
def insider_roster(symbol, external=False, vprint=False):
    """:return: 10 largest insider owners for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'insider-roster', external=external)
    return instance.execute()


#   Insider Summary
IEX_INSIDER_SUMMARY_URL = prepend_iex_url('stock') + '{symbol}/insider-summary?'
def insider_summary(symbol, external=False, vprint=False):
    """:return: Summary of the insiders and their actions within the last 6 months for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'insider-summary', external=external)
    return instance.execute()


#   Insider Transactions
IEX_INSIDER_TRANSACTIONS_URL = prepend_iex_url('stock') + '{symbol}/insider-transactions?'
def insider_transactions(symbol, external=False, vprint=False):
    """:return: Summary of insider transactions for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'insider-transactions', external=external)
    return instance.execute()


#   Institutional Ownership
IEX_INSTITUTIONAL_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/institutional-ownership?'
def institutional_ownership(symbol, external=False, vprint=False):
    """:return: 10 largest instituional owners for the requested ticker. This is defined as explicitly buy or sell-side only.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'institutional-ownership', external=external)
    return instance.execute()


#   IPO Calendar
IEX_UPCOMING_IPOS_URL = prepend_iex_url('stock') + 'market/upcoming-ipos?'
def ipo_upcoming(external=False, vprint=False):
    """:return: List of upcoming IPOs for the current and next month."""
    return iexCommon('stock', 'market', 'upcoming-ipos').execute()


IEX_TODAY_IPOS_URL = prepend_iex_url('stock') + 'market/today-ipos?'
def ipo_today(external=False, vprint=False):
    """:return: List of IPOs happening today."""
    return iexCommon('stock', 'market', 'today-ipos').execute()


#   Key Stats
IEX_STATS_URL = prepend_iex_url('stock') + '{symbol}/stats'
def key_stats(symbol, stat=False, external=False, vprint=False):
    """:return: Important and key statistics for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param stat: The specific stat which you would like to return.
    :type stat: string, optional
    """
    instance = iexCommon('stock', symbol, 'stats', external=external)
    if stat:
        instance.append_subdirectory_to_url(stat)
    return instance.execute()


#   Largest Trades
IEX_LARGEST_TRADES_URL = prepend_iex_url('stock') + '{symbol}/largest-trades?'
def largest_trades(symbol, external=False, vprint=False):
    """:return: Delayed list of largest trades for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'largest-trades', external=external)
    return instance.execute()


#   List
IEX_MARKET_LIST_URL = prepend_iex_url('stock') + '{symbol}/list/{list_type}?'
def market_list(list_type, display_percent=None, external=False, vprint=False):
    """:return: 10 largest companies in the specified list.

    :param list_type: The list that you would like to return.
    :type list_type: accepted values are ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent', 'premarket_losers', 'postmarket_losers', 'premarket_gainers', 'postmarket_gainers'], required
    :param displayPercent: Whether you would like to see the percentage values multiplied by 100
    :type displayPercent: boolean, optional
    """
    instance = iexCommon('stock', symbol, 'list', external=external)
    if list_type:
        instance.append_subdirectory_to_url(list_type)
    if display_percent:
        instance.append_query_params_to_url({'displayPercent' : display_percent})
    return instance.execute()


#   Logo
IEX_LOGO_URL = prepend_iex_url('stock') + '{symbol}/logo?'
def logo(symbol, external=False, vprint=False):
    """:return: Google APIs link to the logo for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'logo', external=external)
    return instance.execute()


#   Market Volume (U.S.)
IEX_MARKET_VOLUME_URL = prepend_iex_url('stock') + 'market/volume?'
def market_volume(format=None, external=False, vprint=False):
    """:return: Market wide trading volume.

    :param format: The output format of the endpoint
    :type format: accepted value is 'csv', optional
    """
    instance = iexCommon('stock', 'market', 'volume')
    if format:
        instance.append_query_params_to_url({'format' : format})
    return instance.execute()


#   News
IEX_NEWS_URL = prepend_iex_url('stock') + '{symbol}/news'
def news(symbol, last=None, external=False, vprint=False):
    """:return: News item summaries for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param last: The number of news items to return.
    :type last: integer, optional
    """
    instance = iexCommon('stock', symbol, 'news', external=external)
    if last:
        instance.append_subdirectory_to_url(last)
    return instance.execute()


#   OHLC
IEX_OHLC_URL = prepend_iex_url('stock') + '{symbol}/ohlc?'
def ohlc(symbol, external=False, vprint=False):
    """:return: Most recent days open, high, low, and close data for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'ohlc', external=external)
    return instance.execute()


#   Peers
IEX_PEERS_URL = prepend_iex_url('stock') + '{symbol}/peers?'
def peers(symbol, external=False, vprint=False):
    """:return: List of a requested ticker's peers.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'peers', external=external)
    return instance.execute()


#   Previous Day Prices
IEX_PREVIOUS_URL = prepend_iex_url('stock') + '{symbol}/previous?'
def previous(symbol, external=False, vprint=False):
    """:return: Previous day's price data for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'previous', external=external)
    return instance.execute()


#   Price
IEX_PRICE_URL = prepend_iex_url('stock') + '{symbol}/price?'
def price(symbol, external=False, vprint=False):
    """:return: Single float value of the requested ticker's price.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'price', external=external)
    return instance.execute()


#   Price Target
IEX_PRICE_TARGET_URL = prepend_iex_url('stock') + '{symbol}/price-target?'
def price_target(symbol, external=False, vprint=False):
    """:return: Analyst's price targets for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'price-target', external=external)
    return instance.execute()


#   Quote
IEX_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/quote'
def quote(symbol, field=None, external=False, vprint=False):
    """:return: rice quote data for the requested ticker. Fields are able to be called individually.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param field: The specific field from the quote endpoint you would like to return.
    :type field: string, optional
    """
    instance = iexCommon('stock', symbol, 'qoute', external=external)
    if field:
        instance.append_subdirectory_to_url(field)
    return instance.execute()


#   Recommended Trends
IEX_RECOMMENDED_TRENDS_URL = prepend_iex_url('stock') + '{symbol}/recommendation-trends?'
def recommendation_trends(symbol, external=False, vprint=False):
    """:return: Analyst recommendations for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'recommendation-trends', external=external)
    return instance.execute()


#   Sector Performance
IEX_SECTOR_PERFORMANCE_URL = prepend_iex_url('stock') + 'market/sector-performance?'
def sector_performance(external=False, vprint=False):
    """:return: Market performance for all sectors."""
    return iexCommon('stock', 'market', 'sector_performance').execute()


#   Splits
IEX_SPLITS_URL = prepend_iex_url('stock') + '{symbol}/splits'
def splits(symbol, scope=None, external=False, vprint=False):
    """:return: Record of stock splits for the requested ticker.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    :param scope: The range of data needed.
    :type scope: accepted arguments: ['5y','2y','1y','ytd','6m','3m','1m','next'], optional
    """
    instance = iexCommon('stock', symbol, 'estimates', external=external)
    if scope:
        instance.append_subdirectory_to_url(scope)
    return instance.execute()


#   Volume by Venue
IEX_VOLUME_BY_VENUE_URL = prepend_iex_url('stock') + '{symbol}/volume-by-venue'
def volume_by_venue(symbol, external=False, vprint=False):
    """:return: rading volume for the requested ticker by venue.

    :param symbol: The ticker or symbol of the stock you would like to request.
    :type symbol: string, required
    """
    instance = iexCommon('stock', symbol, 'volume-by-venue', external=external)
    return instance.execute()
