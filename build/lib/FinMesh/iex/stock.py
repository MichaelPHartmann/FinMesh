from ._common import *

# Advanced Fundementals
IEX_ADVANCED_FUNDEMENTALS_URL = prepend_iex_url('time-series') + 'fundementals/{symbol}/{period}'
def advanced_fundementals(symbol, period, vprint=False, **queries):
    """75,000 credits per symbol requested.
    Returns immediate access to the data points in IEX models for 2850+ companies. Models are updated daily.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    period -> String. Required. The period type of data requested. Accepted are: ['annual','quarterly','ttm']
    All standard time series query parameters are accepted.
    """
    url = replace_url_var(IEX_ADVANCED_FUNDEMENTALS_URL, symbol=symbol, period=period)
    url += '?'
    for key, value in queries.items():
        url += f"&{key}={value}"
    return get_iex_json_request(url, vprint=vprint)


#   Advanced Stats
IEX_ADVANCED_STATS_URL = prepend_iex_url('stock') + '{symbol}/advanced-stats'
def advanced_stats(symbol, vprint=False):
    """3,005 credits per symbol requested.
    Returns everything in key stats plus additional advanced stats such as EBITDA, ratios, key financial data, and more.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_ADVANCED_STATS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Balance Sheet
IEX_BALANCE_SHEET_URL = prepend_iex_url('stock') + '{symbol}/balance-sheet'
def balance_sheet(symbol, period=None, vprint=False, **queries):
    """3,000 credits per symbol requested.
    Returns balance sheet data. Available quarterly or annually with the default being the last available quarter.
    This data is currently only available for U.S. symbols.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    period -> String. Optional. The period type of data requested. Accepted are: ['annual','quarterly']
    last -> String. Optional. the number of periods to return. Max 16 quarterly and 4 annual.
    """
    url = replace_url_var(IEX_BALANCE_SHEET_URL, symbol=symbol)
    if period: url += f'{/period}'
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)


#   Book
IEX_BOOK_URL = prepend_iex_url('stock') + '{symbol}/book?'
def book(symbol, vprint=False):
    """1 credit per symbol requested.
    Returns share book information for the requested stock.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_BOOK_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Cash Flow
IEX_CASH_FLOW_URL = prepend_iex_url('stock') + '{symbol}/cash-flow'
def cash_flow(symbol, period=None, vprint=False, **queries):
    """1,000 credits per symbol requested.
    Returns cash flow data. Available quarterly or annually, with the default being the last available quarter.
    This data is currently only available for U.S. symbols.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    period -> String. Optional. The period type of data requested. Accepted are: ['annual','quarterly']
    last -> String. Optional. The number of periods to return. Max 16 quarterly and 4 annual.
    """
    url = replace_url_var(IEX_CASH_FLOW_URL, symbol=symbol)
    if period: url += f'{/period}'
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)


#   Company
IEX_COMPANY_URL = prepend_iex_url('stock') + '{symbol}/company?'
def company(symbol, vprint=False):
    """1 credit per symbo requested.
    Returns company data such as website, address, and description for the requested ticker.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_COMPANY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Delayed Quote
IEX_DELAYED_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/delayed-quote?'
def delayed_quote(symbol, vprint=False):
    """1 credit per symbol requested.
    Returns a 15-minute delayed market quote for the requested ticker.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_DELAYED_QUOTE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Dividends
IEX_DIVIDENDS_URL = prepend_iex_url('stock') + '{symbol}/dividends/{scope}?'
def dividends(symbol, scope, vprint=False):
    """10 credits per symbol requested.
    Provides basic dividend data for US equities, ETFs, and Mutual Funds for the last 5 years.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    scope -> String. Required. The range of data required. ('5y', 'ytd', '1m', 'next', etc.)
    """
    url = replace_url_var(IEX_DIVIDENDS_URL, symbol=symbol, scope=scope)
    return get_iex_json_request(url, vprint=vprint)


#   Financials
IEX_FINANCIALS_URL = prepend_iex_url('stock') + '{symbol}/financials'
def financials(symbol, period=None, vprint=False):
    """5,000 credits per symbol requested.
    Pulls income statement, balance sheet, and cash flow data from the most recent reported quarter.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    period -> String. Optional. The period type of data requested. Accepted are: ['annual','quarterly']
    """
    url = replace_url_var(IEX_FINANCIALS_URL, symbol=symbol)
    if period: url += f'{/period}'
    url += '?'
    return get_iex_json_request(url, vprint=vprint)


#   Financials as Reported
IEX_FINANCIALS_REPORTED_URL = prepend_iex_url('time-series') + 'reported_financials/{symbol}/{filing}?'
def financials_as_reported(symbol, filing, specification=None, vprint=False):
    """5,000 credits per symbol requested.
    As reported financials are pulled directly from the raw SEC filings.
    Returns raw financial data reported in 10-K and 10-Q filings.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    filing -> String. Required. The filing type you wish to retrieve. Accepted are ['10-K','10-Q']
    All standard time series query parameters are accepted.
    """
    url = replace_url_var(IEX_FINANCIALS_REPORTED_URL, symbol=symbol, filing=filing)
    if specification:
        url =+ specification
    ## Needs support for specific queries of date-specific or n-last filings
    return get_iex_json_request(url, vprint=vprint)


#   Fund Ownership
IEX_FUND_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/fund-ownership?'
def fund_ownership(symbol, vprint=False):
    """10,000 credits per symbol requested.
    Returns the top 10 fund holders by default, meaning any firm not defined as buy-side or sell-side.
    Full ownership is available by using time series API.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_FUND_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


IEX_HISTORICAL_URL = prepend_iex_url('stock')
def new_historical_price(symbol, period, date=None, chart_by_day=False, chart_close_only=False, vprint=False):
    # This endpoint sucks in it's current form.
    # This is probably the best way to handle this for now.
    url = IEX_HISTORICAL_URL + f"{symbol}/chart/{period}"
    if period == 'date':
        url += f'/{date}'
    url = append_iex_token(url)
    if chart_by_day:
        url += 'chartByDay=True'
    if chart_close_only:
        url += 'chartCloseOnly=True'
    result = requests.get(url)
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
new_historical_price.__doc__='Returns the historical price for the requested stock.'

IEX_HISTORICAL_URL = prepend_iex_url('stock')
def historical_price(symbol, period, date=None, chart_by_day=False, vprint=False, **queries):
    # Returns the historical price for the requested ticker.
    # Soon to be deprecated
    # Here the query string parameters are handled a bit differently because
    # there are so many.  This may be inconsistent but no other way is realistic
    url = IEX_HISTORICAL_URL + f"{symbol}/chart/{period}"
    if period == 'date':
        url += f'/{date}'
        if chart_by_day:
            url += '?&chartByDay=True'
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
historical_price.__doc__='Returns the historical price for the requested stock.'

#   Income Statement
IEX_INCOME_STATEMENT_URL = prepend_iex_url('stock') + '{symbol}/income'
def income_statement(symbol, period=None, vprint=False, **queries):
    """1,000 credits per symbol requested.
    Returns income statement data. Available quarterly or annually, with the default being the last available quarter.
    This data is currently only available for U.S. symbols.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    period -> String. Optional. The period type of data requested. Accepted are: ['annual','quarterly']
    last -> String. Optional. The number of periods to return. Max 16 quarterly and 4 annual.
    """
    url = replace_url_var(IEX_INCOME_STATEMENT_URL, symbol=symbol)
    if period: url += f'/{period}'
    url += '?'
    for key, value in queries.items():
        url += (f"&{key}={value}")
    return get_iex_json_request(url, vprint=vprint)


#   Insider Roster
IEX_INSIDER_ROSTER_URL = prepend_iex_url('stock') + '{symbol}/insider-roster?'
def insider_roster(symbol, vprint=False):
    """5,000 credits per symbol requested.
    Returns the top 10 insiders, with the most recent information.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_INSIDER_ROSTER_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Insider Summary
IEX_INSIDER_SUMMARY_URL = prepend_iex_url('stock') + '{symbol}/insider-summary?'
def insider_summary(symbol, vprint=False):
    """5,000 credits per symbol requested.
    Returns aggregated insiders summary data for the last 6 months.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_INSIDER_SUMMARY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Insider Transactions
IEX_INSIDER_TRANSACTIONS_URL = prepend_iex_url('stock') + '{symbol}/insider-transactions?'
def insider_transactions(symbol, vprint=False):
    """50 credits per transaction requested.
    Returns insider transactions.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_INSIDER_TRANSACTIONS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Institutional Ownership
IEX_INSTITUTIONAL_OWNERSHIP_URL = prepend_iex_url('stock') + '{symbol}/institutional-ownership?'
def institutional_ownership(symbol, vprint=False):
    """Returns the top 10 institutional holders by default, defined as buy-side or sell-side firms.
    Full ownership is available by using time series API.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_INSTITUTIONAL_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Intraday Prices
IEX_INTRADAY_URL = prepend_iex_url('stock') + '{symbol}/intraday-prices'
def intraday_prices(symbol, vprint=False):
    """1 credit per symbol per time interval up to a max use of 50 credits.
    This endpoint will return aggregated intraday prices in one-minute buckets for the current day.
    For historical intraday data, use our Historical Prices endpoint.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_INTRADAY_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   IPO Calendar
# May be deprecated
IEX_UPCOMING_IPOS_URL = prepend_iex_url('stock') + 'market/upcoming-ipos?'
def ipo_upcoming(vprint=False):
    """Returns a list of upcoming IPOs for the current and next month."""
    return get_iex_json_request(IEX_UPCOMING_IPOS_URL)


# May be deprecated
IEX_TODAY_IPOS_URL = prepend_iex_url('stock') + 'market/today-ipos?'
def ipo_today(vprint=False):
    """Returns a list of IPOs happening today."""
    return get_iex_json_request(IEX_TODAY_IPOS_URL)


#   Key Stats
IEX_STATS_URL = prepend_iex_url('stock') + '{symbol}/stats?'
def key_stats(symbol, stat=None, vprint=False):
    """5 credits per symbol requested.
    Returns important and key statistics for the requested ticker.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_STATS_URL, symbol=symbol)
    if stat:
        url += str(stat) + '?'
    else: '?'
    return get_iex_json_request(url, vprint=vprint)


#   Largest Trades
IEX_LARGEST_TRADES_URL = prepend_iex_url('stock') + '{symbol}/largest-trades?'
def largest_trades(symbol, vprint=False):
    """1 credit per trade requested.
    This returns 15 minute delayed, last sale eligible trades.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_LARGEST_TRADES_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Logo
IEX_LOGO_URL = prepend_iex_url('stock') + '{symbol}/logo?'
def logo(symbol, vprint=False):
    """1 credit per logo requested.
    Returns a Google APIs link to the logo for the requested ticker.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_LOGO_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   News
IEX_NEWS_URL = prepend_iex_url('stock') + '{symbol}/news'
def news(symbol, last=None, vprint=False):
    url = replace_url_var(IEX_NEWS_URL, symbol=symbol)
    url += f'/last/{last}?' if last else '?'
    return get_iex_json_request(url, vprint=vprint)


#   OHLC
IEX_OHLC_URL = prepend_iex_url('stock') + '{symbol}/ohlc?'
def ohlc(symbol, vprint=False):
    """2 credits per symbol requested.
    Returns the official open and close for a give symbol.
    The official open is available as soon as 9:45am ET and the official close as soon as 4:15pm ET.
    Some stocks can report late open or close prices.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_OHLC_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Peers
IEX_PEERS_URL = prepend_iex_url('stock') + '{symbol}/peers?'
def peers(symbol, vprint=False):
    """500 credits per call.
    Returns a list of a requested stocks peers.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_PEERS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Price
IEX_PRICE_URL = prepend_iex_url('stock') + '{symbol}/price?'
def price(symbol, vprint=False):
    """Returns a single float value of the requested company\'s price.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_PRICE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)


#   Quote
IEX_QUOTE_URL = prepend_iex_url('stock') + '{symbol}/quote'
def quote(symbol, field=None, vprint=False):
    """1 credit per quote requested.
    Returns price quote data for the requested stock. Fields are able to be called individually.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_QUOTE_URL, symbol=symbol)
    url += f'/{field}?' if field else '?'
    return get_iex_json_request(url, vprint=vprint)


#   Sector Performance
IEX_SECTOR_PERFORMANCE_URL = prepend_iex_url('stock') + 'market/sector-performance?'
def sector_performance(vprint=False):
    # Returns market performance for all sectors.
    return get_iex_json_request(IEX_SECTOR_PERFORMANCE_URL)
sector_performance.__doc__='Returns market performance for all sectors. No longer listed in docs, may soon be deprecated.'


#   Splits
IEX_SPLITS_URL = prepend_iex_url('stock') + '{symbol}/splits'
def splits(symbol, scope=None, vprint=False):
    # Returns a record of stock splits for the requested ticker.
    url = replace_url_var(IEX_SPLITS_URL, symbol=symbol)
    url += f'/{scope}?' if scope else '?'
    return get_iex_json_request(url, vprint=vprint)


#   Technical Indicators
IEX_TECHNICAL_URL = prepend_iex_url('stock') + '{symbol}/indicator/{indicator_name}'
def technical_indicators(symbol, indicator, vprint=False):
    """50 credits per symbol requested.
    Technical indicators are available for any historical or intraday range.
    This endpoint calls the historical or intraday price endpoints for the given range, and the associated indicator for the price range.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    indicator -> String. Required. The name of the indicator you wish to lookup.
    """
    url = replace_url_var(IEX_TECHNICAL_URL, symbol=symbol, indicator_name=indicator)
    return get_iex_json_request(url, vprint=vprint)


#   Volume by Venue
IEX_VOLUME_BY_VENUE_URL = prepend_iex_url('stock') + '{symbol}/volume-by-venue'
def volume_by_venue(symbol, vprint=False):
    """This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    Parameters:
    symbol -> String. Required. The ticker or symbol of the company for which you would like information.
    """
    url = replace_url_var(IEX_VOLUME_BY_VENUE_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
