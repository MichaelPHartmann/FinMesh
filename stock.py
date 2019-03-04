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

def _append_token(url):
    token = os.getenv('IEX_TOKEN')
    return "{}&token={}".format(url, token)

#   Balance Sheet
IEX_STOCK_BALANCE_SHEET_URL = IEX_STOCK_BASE_URL + '{symbol}/balance-sheet?period={period}'
def balance_sheet(symbol, period):
    url = IEX_STOCK_BALANCE_SHEET_URL
    url = url.replace('{symbol}', symbol)
    url = url.replace('{period}', period)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Batch Requests
def batch_requests():
    raise ImplementationError("Function cannot be implemented.")

#   Book
IEX_STOCK_BOOK_URL = IEX_STOCK_BASE_URL + '{symbol}/book?'
def book(symbol):
    url = IEX_STOCK_BOOK_URL
    url = url.replace('{symbol}', symbol)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Cash Flow
IEX_STOCK_CASH_FLOW_URL = IEX_STOCK_BASE_URL + '{symbol}/cash_flow?'
def cash_flow(symbol, period=None):
    url = IEX_STOCK_CASH_FLOW_URL
    url = url.replace('{symbol}', symbol)
    if period:
        url = url + "period={}".format(period)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Collections
IEX_STOCK_COLLECTION_URL = IEX_STOCK_BASE_URL + 'market/collection/{collectionType}?collectionName={collectionName}'
def collection(collectionType, collectionName):
    url = IEX_STOCK_COLLECTION_URL
    url = url.replace('{collectionType}', collectionType)
    url = url.replace('{collectionName}', collectionName)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Company
IEX_STOCK_COMPANY_URL = IEX_STOCK_BASE_URL + '{symbol}/company'
def company(symbol):
    url = IEX_STOCK_COMPANY_URL
    url = url.replace('{symbol}', symbol)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Delayed Quote
IEX_STOCK_DELAYED_QUOTE_URL = IEX_STOCK_BASE_URL + '{symbol}/delayed-quote'
def delayed_quote(symbol):
    url = IEX_STOCK_DELAYED_QUOTE_URL
    url = url.replace('{symbol}', symbol)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Dividends
IEX_DIVIDENDS_QUOTE_URL = IEX_STOCK_BASE_URL + 'stock/{symbol}/dividends/{range}'
def dividends(symbol, range):
    url = IEX_DIVIDENDS_QUOTE_URL
    url = url.replace('{symbol}', symbol)
    url = url.replace('{range}', range)
    result = requests.get(_append_token(url))
    result = result.json()
    return result

#   Earnings
#   Earnings Today
#   Effective Spread
#   Estimates
#   Financials
#   Fund Ownership
#   Historical Prices
#   Income Statement
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



# Returns historical stock prices for specified company
IEX_STOCK_CHART_URL = IEXCLOUD_STOCK_BASE_URL + '{symbol}/chart/{range}/{date}'
def chart(symbol, range, date='', format=None):
    url = IEX_STOCK_CHART_URL.replace('{symbol}', symbol).replace('{range}', range).replace('{date}', date)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns financials overview (limited data) for specified company
IEX_STOCK_FINANCIALS_URL = IEXCLOUD_STOCK_BASE_URL + '{symbol}/financials?period={period}'
def financials(symbol, period, format=None):
    url = IEX_STOCK_FINANCIALS_URL.replace('{symbol}', symbol).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns income statement for specified company
IEX_STOCK_INCOME_STATEMENT_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/income?period={period}'
def income_statement(symbol, period, format=None):
    url = IEX_STOCK_INCOME_STATEMENT_URL.replace('{symbol}', symbol).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns balance sheet for specified company
IEX_STOCK_BALANCE_SHEET_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/balance-sheet?period={period}'
def balance_sheet(symbol, period, format=None):
    url = IEX_STOCK_BALANCE_SHEET_URL.replace('{symbol}', symbol).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns cash flow statement for specified company
IEX_STOCK_CASH_FLOW_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/cash-flow?period={period}'
def cash_flow(symbol, period, format=None):
    url = IEX_STOCK_CASH_FLOW_URL.replace('{symbol}', symbol).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns key statistics for specified company
IEX_STOCK_KEY_STAT_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/stats/{stat}'
def key_stat(symbol, stat, format=None):
    url = IEX_STOCK_KEY_STAT_URL.replace('{symbol}', symbol).replace('{stat}', stat)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns the analyst price target for specified company
IEX_STOCK_PRICE_TARGET_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/price-target'
def price_target(symbol, format=None):
    url = IEX_STOCK_PRICE_TARGET_URL.replace('{symbol}', symbol)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns dividend information for specified company
IEX_STOCK_DIVIDENDS_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/dividends/{range}'
def dividends(symbol, range, format=None):
    url = IEX_STOCK_DIVIDENDS_URL.replace('{symbol}', symbol).replace('{range}', range)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns relevant stocks, similar to peers (true/false specifies whether it is the peer list)
IEX_STOCK_RELEVANT_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/relevant'
def relevant(symbol, format=None):
    url = IEX_STOCK_RELEVANT_URL.replace('{symbol}')
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns IB analyst recommendations
IEX_STOCK_RECOMENDATION_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/recommendation-trends'
def recommendation_trends(symbol, format=None):
    url = IEX_STOCK_RECOMENDATION_URL.replace('{symbol}', symbol)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns earnings estimates for the specified company
IEX_STOCK_ESTIMATES_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/estimates'
def analyst_estimates(symbol, format=None):
    url = IEX_STOCK_ESTIMATES_URL.replace('{symbol}', symbol)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

# Returns 10 most recent news items for specified company
IEX_STOCK_NEWS_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{symbol}/news'
def news(symbol, format=None):
    url = IEX_STOCK_NEWS_URL.replace('{symbol}', symbol)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result
