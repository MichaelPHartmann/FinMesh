from iex._common import *

SAND_BOX = False

if SAND_BOX:
    IEX_STOCK_BASE_URL = 'https://sandbox.iexapis.com/beta/stock/'
else:
    IEX_STOCK_BASE_URL = 'https://cloud.iexapis.com/beta/stock/'

#   Balance Sheet
IEX_BALANCE_SHEET_URL = IEX_STOCK_BASE_URL + '{symbol}/balance-sheet'
def balance_sheet(symbol, period=None, last=None, field=None):
    url = replace_url_var(IEX_BALANCE_SHEET_URL, symbol=symbol)
    if last: url += f'/{last}'
    if field: url += f'{field}'
    if period: url += f'/period={period}'
    url += '?'
    return get_iex_json_request(url)

#   Batch Requests
def batch_requests():
    raise ImplementationError("Function cannot be implemented.")

#   Book
IEX_BOOK_URL = IEX_STOCK_BASE_URL + '{symbol}/book?'
def book(symbol):
    url = replace_url_var(IEX_BOOK_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Cash Flow

IEX_CASH_FLOW_URL = IEX_STOCK_BASE_URL + '{symbol}/cash-flow'
def cash_flow(symbol, period=None, last=None, field=None):
    url = replace_url_var(IEX_CASH_FLOW_URL, symbol=symbol)
    if last: url += f'/{last}'
    if field: url += f'{field}'
    if period: url += f'/period={period}'
    url += '?'
    return get_iex_json_request(url)

#   Collections
IEX_COLLECTION_URL = IEX_STOCK_BASE_URL + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName):
    url = replace_url_var(IEX_COLLECTION_URL, collectionType=collectionType, collectionName=collectionName)
    return get_iex_json_request(url)

#   Company
IEX_COMPANY_URL = IEX_STOCK_BASE_URL + '{symbol}/company?'
def company(symbol):
    url = replace_url_var(IEX_COMPANY_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Delayed Quote
IEX_DELAYED_QUOTE_URL = IEX_STOCK_BASE_URL + '{symbol}/delayed-quote?'
def delayed_quote(symbol):
    url = replace_url_var(IEX_DELAYED_QUOTE_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Dividends
IEX_DIVIDENDS_URL = IEX_STOCK_BASE_URL + '{symbol}/dividends/{scope}?'
def dividends(symbol, scope):
    url = replace_url_var(IEX_DIVIDENDS_URL, symbol=symbol, scope=scope)
    return get_iex_json_request(url)

#   Earnings
IEX_EARNINGS_URL = IEX_STOCK_BASE_URL + '{symbol}/earnings'
def earnings(symbol, last=None, field=None):
    url = replace_url_var(IEX_EARNINGS_URL, symbol=symbol)
    if last and field:
        url+= f"/{last}/{field}?"
    elif last:
        url+= f"/{last}?"
    else:
        url += '?'
    return get_iex_json_request(url)

#   Earnings Today
IEX_TODAY_EARNINGS_URL = IEX_STOCK_BASE_URL + 'market/today-earnings?'
def today_earnings():
    url = IEX_TODAY_EARNINGS_URL
    return get_iex_json_request(url)

#   Effective Spread
IEX_EFFECTIVE_SPREAD_URL = IEX_STOCK_BASE_URL + '{symbol}/effective-spread?'
def effective_spread(symbol):
    url = replace_url_var(IEX_EFFECTIVE_SPREAD_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Estimates
IEX_ESTIMATES_URL = IEX_STOCK_BASE_URL + '{symbol}/estimates?'
def estimates(symbol):
    url = replace_url_var(IEX_ESTIMATES_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Financials
IEX_FINANCIALS_URL = IEX_STOCK_BASE_URL + '{symbol}/financials?'
def financials(symbol, period=None):
    url = replace_url_var(IEX_FINANCIALS_URL, symbol=symbol)
    url += f'period={period}' if period else ''
    return get_iex_json_request(url)

#   Fund Ownership
IEX_FUND_OWNERSHIP_URL = IEX_STOCK_BASE_URL + '{symbol}/fund-ownership?'
def fund_ownership(symbol):
    url = replace_url_var(IEX_FUND_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url)

IEX_HISTORICAL_URL = IEX_STOCK_BASE_URL + '{symbol}/chart'
def historical_price(symbol, scope=None, dynamic=False, **kwargs):
#   Soon to be deprecated
#   Here the query string parameters are handled a bit differently because
#   there are so many.  This may be inconsistent but no other way is realistic
    url = replace_url_var(IEX_HISTORICAL_URL, symbol=symbol, scope=None, dynamic=None, **kwargs, status=False)
    if scope: url += f'/{scope}'
    if dynamic: url += f'/dynamic'
    url += '?'
    url = append_iex_token(url)
    for key, value in kwargs.items():
        url += f'&{key}={value}'
    if status: print(f"Now fetching: {url}")
    result = requests.get(url)
    if status: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

#   DEPRECATED in favour of historical prices as to align
#   with IEX nomenclature
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#IEX_CHART_URL = IEX_STOCK_BASE_URL + '{symbol}/chart'
#def chart(symbol, scope=None, date=None, dynamic=False, **kwargs):
#    url = replace_url_var(IEX_CHART_URL, symbol=symbol)
#    if scope:
#        url+= f'/{scope}?'
#    elif dynamic:
#        url+= f'/dynamic?'
#    else:
#        url+= '?'
#    for key, value in kwargs.items():
#        url += f'&{key}={value}'
#
#    return get_iex_json_request(url)

#   Income Statement
IEX_INCOME_STATEMENT_URL = IEX_STOCK_BASE_URL + '{symbol}/income'
def income_statement(symbol, period=None, last=None, field=None):
    url = replace_url_var(IEX_INCOME_STATEMENT_URL, symbol=symbol)
    if last: url += f'/{last}'
    if field: url += f'{field}'
    if period: url += f'/period={period}'
    url += '?'
    return get_iex_json_request(url)

#   Insider Roster
IEX_INSIDER_ROSTER_URL = IEX_STOCK_BASE_URL + '{symbol}/insider-roster?'
def insider_roster(symbol):
    url = replace_url_var(IEX_INSIDER_ROSTER_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Insider Summary
IEX_INSIDER_SUMMARY_URL = IEX_STOCK_BASE_URL + '{symbol}/insider-summary?'
def insider_summary(symbol):
    url = replace_url_var(IEX_INSIDER_SUMMARY_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Insider Transactions
IEX_INSIDER_TRANSACTIONS_URL = IEX_STOCK_BASE_URL + '{symbol}/insider-transactions?'
def insider_transactions(symbol):
    url = replace_url_var(IEX_INSIDER_TRANSACTIONS_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Institutional Ownership
IEX_INSTITUTIONAL_OWNERSHIP_URL = IEX_STOCK_BASE_URL + '{symbol}/institutional-ownership?'
def institutional_ownership(symbol):
    url = replace_url_var(IEX_INSTITUTIONAL_OWNERSHIP_URL, symbol=symbol)
    return get_iex_json_request(url)

#   IPO Calendar
IEX_UPCOMING_IPOS_URL = IEX_STOCK_BASE_URL + 'market/upcoming-ipos?'
def ipo_upcoming():
    return get_iex_json_request(IEX_UPCOMING_IPOS_URL)

IEX_TODAY_IPOS_URL = IEX_STOCK_BASE_URL + 'market/today-ipos?'
def ipo_today():
    return get_iex_json_request(IEX_TODAY_IPOS_URL)

#   Key Stats
IEX_STATS_URL = IEX_STOCK_BASE_URL + '{symbol}/stats'
def key_stats(symbol, stat=False):
    url = replace_url_var(IEX_STATS_URL, symbol=symbol)
    url += str(stat) if stat else '?'
    return get_iex_json_request(url)

#   Largest Trades
IEX_LARGEST_TRADES_URL = IEX_STOCK_BASE_URL + '{symbol}/largest-trades?'
def largest_trades(symbol):
    url = replace_url_var(IEX_LARGEST_TRADES_URL, symbol=symbol)
    return get_iex_json_request(url)

#   List
IEX_MARKET_LIST_URL = IEX_STOCK_BASE_URL + '{symbol}/list/{list_type}?'
def market_list(symbol, list_type, displayPercent=None):
    url = replace_url_var(IEX_MARKET_LIST_URL, symbol=symbol, list_type=list_type)
    url += f'displayPercent={displayPercent}' if displayPercent else ''
    return get_iex_json_request(url)

#   Logo
IEX_LOGO_URL = IEX_STOCK_BASE_URL + '{symbol}/logo?'
def logo(symbol):
    url = replace_url_var(IEX_LOGO_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Market Volume (U.S.)
IEX_MARKET_VOLUME_URL = IEX_STOCK_BASE_URL + 'market/volume?'
def market_volume(format=None):
    url = IEX_MARKET_VOLUME_URL
    url += f'format={format}' if format else ''
    return get_iex_json_request(url)

#   News
IEX_NEWS_URL = IEX_STOCK_BASE_URL + '{symbol}/news'
def news(symbol, last=None):
    url = replace_url_var(IEX_NEWS_URL, symbol=symbol)
    url += f'/last/{last}?' if last else '?'
    return get_iex_json_request(url)

#   OHLC
IEX_OHLC_URL = IEX_STOCK_BASE_URL + '{symbol}/ohlc?'
def ohlc(symbol):
    url = replace_url_var(IEX_OHLC_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Open / Close Price
#       Does not have cooresponding endpoint

#   Peers
IEX_PEERS_URL = IEX_STOCK_BASE_URL + '{symbol}/peers?'
def peers(symbol):
    url = replace_url_var(IEX_PEERS_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Previous Day Prices
IEX_PREVIOUS_URL = IEX_STOCK_BASE_URL + '{symbol}/previous?'
def previous(symbol):
    url = replace_url_var(IEX_PREVIOUS_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Price
IEX_PRICE_URL = IEX_STOCK_BASE_URL + '{symbol}/price?'
def price(symbol):
    url = replace_url_var(IEX_PRICE_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Price Target
IEX_PRICE_TARGET_URL = IEX_STOCK_BASE_URL + '{symbol}/price-target?'
def price_target(symbol):
    url = replace_url_var(IEX_PRICE_TARGET_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Quote
IEX_QUOTE_URL = IEX_STOCK_BASE_URL + '{symbol}/quote'
def quote(symbol, field=None):
    url = replace_url_var(IEX_QUOTE_URL, symbol=symbol)
    url += f'/{field}?' if field else '?'
    return get_iex_json_request(url)

#   Recommended Trends
IEX_RECOMMENDED_TRENDS_URL = IEX_STOCK_BASE_URL + '{symbol}/recommendation-trends?'
def recommendation_trends(symbol):
    url = replace_url_var(IEX_RECOMMENDED_TRENDS_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Relavent Stocks
IEX_RELEVANT_URL = IEX_STOCK_BASE_URL + '{symbol}/relevant?'
def relevant(symbol):
    url = replace_url_var(IEX_RELEVANT_URL, symbol=symbol)
    return get_iex_json_request(url)

#   Sector Performance
IEX_SECTOR_PERFORMANCE_URL = IEX_STOCK_BASE_URL + 'market/sector-performance?'
def sector_performance():
    return get_iex_json_request(IEX_SECTOR_PERFORMANCE_URL)

#   Splits
IEX_SPLITS_URL = IEX_STOCK_BASE_URL + '{symbol}/splits'
def splits(symbol, scope=None):
    url = replace_url_var(IEX_SPLITS_URL, symbol=symbol)
    url += f'/{scope}?' if scope else '?'
    return get_iex_json_request(url)

#   Volume by Venue
IEX_VOLUME_BY_VENUE_URL = IEX_STOCK_BASE_URL + '{symbol}/volume-by-venue'
def volume_by_venue(symbol):
    url = replace_url_var(IEX_VOLUME_BY_VENUE_URL, symbol=symbol)
    return get_iex_json_request(url)
