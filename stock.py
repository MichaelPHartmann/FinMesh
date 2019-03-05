import requests
import os

# API Endpoints for "stock":
#   Balance Sheet
#   Batch Requests
#   Book
#   Cash Flow
#   Collections
#   Company
#   Delayed Quote
#   Dividends
#   Earnings
#   Earnings Today
#   Effective Spread
#   Estimates
#   Financials
#   Fund Ownership
#   Historical Prices
#   Income Statement
#   Insider Roster
#   Insider Summary
#   Insider Transactions

#   Institutional Ownership
#   IPO Calendar
#   Key Stats
#   Largest Trades
#   List
#   Logo
#   Market Volume (U.S.)
#   News
#   OHLC
#   Open / Close Price
#   Peers
#   Previous Day Prices
#   Price
#   Price Target
#   Quote
#   Recommended Trends
#   Relavent Stocks
#   Sector Performance
#   Splits
#   Volume by Venue

IEX_STOCK_BASE_URL = 'https://cloud.iexapis.com/beta/stock/'
VERBOSE = False # Turn on explanitory output


def _vprint(*args, **kwargs):
    if VERBOSE:
        print(*args, **kwargs)

def _append_token(url):
    token = os.getenv('IEX_TOKEN')
    return f"{url}&token={token}"

def _get_iex_json_request(url):
    url = _append_token(url)
    _vprint(f"Making request: {url}")
    result = requests.get(url)
    _vprint(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

def _replace_url_var(url, **kwargs):
    for key, value in kwargs.items():
        url = url.replace('{' + key + '}', value)
    return url


#   Balance Sheet
IEX_BALANCE_SHEET_URL = IEX_STOCK_BASE_URL + '{symbol}/balance-sheet?period={period}'
def balance_sheet(symbol, period):
    url = _replace_url_var(IEX_BALANCE_SHEET_URL, symbol=symbol, period=period)
    return _get_iex_json_request(url)

#   Batch Requests
def batch_requests():
    raise ImplementationError("Function cannot be implemented.")

#   Book
IEX_BOOK_URL = IEX_STOCK_BASE_URL + '{symbol}/book?'
def book(symbol):
    url = _replace_url_var(IEX_BOOK_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Cash Flow
IEX_CASH_FLOW_URL = IEX_STOCK_BASE_URL + '{symbol}/cash_flow?'
def cash_flow(symbol, period=None):
    url = _replace_url_var(IEX_CASH_FLOW_URL, symbol=symbol)
    if period:
        url = url + f"period={period}"
    return _get_iex_json_request(url)

#   Collections
IEX_COLLECTION_URL = IEX_STOCK_BASE_URL + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName):
    url = _replace_url_var(IEX_COLLECTION_URL, collectionType=collectionType, collectionName=collectionName)
    return _get_iex_json_request(url)

#   Company
IEX_COMPANY_URL = IEX_STOCK_BASE_URL + '{symbol}/company?'
def company(symbol):
    url = _replace_url_var(IEX_COMPANY_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Delayed Quote
IEX_DELAYED_QUOTE_URL = IEX_STOCK_BASE_URL + '{symbol}/delayed-quote?'
def delayed_quote(symbol):
    url = _replace_url_var(IEX_DELAYED_QUOTE_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Dividends
IEX_DIVIDENDS_URL = IEX_STOCK_BASE_URL + '{symbol}/dividends/{range}?'
def dividends(symbol, range):
    url = _replace_url_var(IEX_DIVIDENDS_URL, symbol=symbol, range=range)
    return _get_iex_json_request(url)

#   Earnings
IEX_EARNINGS_URL = IEX_STOCK_BASE_URL + '{symbol}/earnings?'
def earnings(symbol, last=None, field=None):
    url = _replace_url_var(IEX_EARNINGS_URL, symbol=symbol)
    if last:
        url = url + f"/{last}"
        if field:
            url = url + f"/{field}"
    return _get_iex_json_request(url)

#   Earnings Today
IEX_TODAY_EARNINGS_URL = IEX_STOCK_BASE_URL + 'market/today-earnings?'
def today_earnings():
    url = IEX_TODAY_EARNINGS_URL
    return _get_iex_json_request(url)

#   Effective Spread
IEX_EFFECTIVE_SPREAD_URL = IEX_STOCK_BASE_URL + '{symbol}/effective-spread?'
def effective_spread(symbol):
    url = _replace_url_var(IEX_EFFECTIVE_SPREAD_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Estimates
IEX_ESTIMATES_URL = IEX_STOCK_BASE_URL + '{symbol}/estimates?'
def estimates(symbol):
    url = _replace_url_var(IEX_ESTIMATES_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Financials
IEX_FINANCIALS_URL = IEX_STOCK_BASE_URL + '{symbol}/financials?'
def financials(symbol, period=None):
    url = _replace_url_var(IEX_FINANCIALS_URL, symbol=symbol)
    if period:
        url = url + f"period={period}"
    return _get_iex_json_request(url)

#   Fund Ownership
IEX_FUND_OWNERSHIP_URL = IEX_STOCK_BASE_URL + '{symbol}/fund-ownership?'
def fund_ownership(symbol):
    url = _replace_url_var(IEX_FUND_OWNERSHIP_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Historical Prices
IEX_CHART_URL = IEX_STOCK_BASE_URL + '{symbol}/chart'
def chart(symbol, range=None, date=None, chartByDay=False, dynamic=False):
    url = _replace_url_var(IEX_CHART_URL, symbol=symbol)
    if range:
        url = url + f'/{range}?'
    elif date:
        url = url + f'/date/{date}?chartByDay={chartByDay}'
    elif dynamic:
        url = url + f'/dynamic?'
    else:
        url = url + '?'
    return _get_iex_json_request(url)

#   Income Statement
IEX_INCOME_URL = IEX_STOCK_BASE_URL + '{symbol}/income?'
def income(symbol, period=None):
    url = _replace_url_var(IEX_INCOME_URL, symbol=symbol)
    if period:
        url = url + f'period={period}'
    return _get_iex_json_request(url)

#   Insider Roster
IEX_INSIDER_ROSTER_URL = IEX_STOCK_BASE_URL + '{symbol}/insider-roster?'
def insider_roster(symbol):
    url = _replace_url_var(IEX_INSIDER_ROSTER_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Insider Summary
IEX_INSIDER_SUMMARY_URL = IEX_STOCK_BASE_URL + '{symbol}/insider-summary?'
def insider_summary(symbol):
    url = _replace_url_var(IEX_INSIDER_SUMMARY_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Insider Transactions
IEX_INSIDER_TRANSACTIONS_URL = IEX_STOCK_BASE_URL + '{symbol}/insider-transactions?'
def insider_transactions(symbol):
    url = _replace_url_var(IEX_INSIDER_TRANSACTIONS_URL, symbol=symbol)
    return _get_iex_json_request(url)

#   Institutional Ownership
#   IPO Calendar
#   Key Stats
#   Largest Trades
#   List
#   Logo
#   Market Volume (U.S.)
#   News
#   OHLC
#   Open / Close Price
#   Peers
#   Previous Day Prices
#   Price
#   Price Target
#   Quote
#   Recommended Trends
#   Relavent Stocks
#   Sector Performance
#   Splits
#   Volume by Venue


if __name__ == '__main__':
    import json
    print("Running Developer Tests...")
    VERBOSE = True
