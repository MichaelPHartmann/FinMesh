import requests
import os

#{ticker} replaces the IEX-defined {symbol} in every case.
#In all other instances naming is identical to the IEX API
#Single quotes ('') only :)

#API Endpoints taken care of here:
#Account usage
#Chart
#Financials
#Income Statement
#Balance Sheet
#Cash Flow Statement
#Key Stats
#Price Target
#Dividends
#Relevant
#Recommendation Trends
#Analyst Estimates
#News

IEXCLOUD_STOCK_BASE_URL = 'https://cloud.iexapis.com/beta/stock/'

def append_token(url):
    token = os.getenv('IEX_TOKEN')
    return "{}?token={}".format(url, token)

#Returns your account usage data, with option to return only specific datapoints
IEX_STOCK_ACCOUNT_USAGE_URL = IEXCLOUD_STOCK_BASE_URL + 'account/usage/{type}'
def account_usage(type="", format=None):
    url = IEX_STOCK_ACCOUNT_USAGE_URL.replace('{type}', type)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns historical stock prices for specified company
IEX_STOCK_CHART_URL = IEXCLOUD_STOCK_BASE_URL + '{ticker}/chart/{range}/{date}'
def chart(ticker, range, date='', format=None):
    url = IEX_STOCK_CHART_URL.replace('{ticker}', ticker).replace('{range}', range).replace('{date}', date)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns financials overview (limited data) for specified company
IEX_STOCK_FINANCIALS_URL = IEXCLOUD_STOCK_BASE_URL + '{ticker}/financials?period={period}'
def financials(ticker, period, format=None):
    url = IEX_STOCK_FINANCIALS_URL.replace('{ticker}', ticker).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns income statement for specified company
IEX_STOCK_INCOME_STATEMENT_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/income?period={period}'
def income_statement(ticker, period, format=None):
    url = IEX_STOCK_INCOME_STATEMENT_URL.replace('{ticker}', ticker).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns balance sheet for specified company
IEX_STOCK_BALANCE_SHEET_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/balance-sheet?period={period}'
def balance_sheet(ticker, period, format=None):
    url = IEX_STOCK_BALANCE_SHEET_URL.replace('{ticker}', ticker).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns cash flow statement for specified company
IEX_STOCK_CASH_FLOW_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/cash-flow?period={period}'
def cash_flow(ticker, period, format=None):
    url = IEX_STOCK_CASH_FLOW_URL.replace('{ticker}', ticker).replace('{period}', period)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns key statistics for specified company
IEX_STOCK_KEY_STAT_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/stats/{stat}'
def key_stat(ticker, stat, format=None):
    url = IEX_STOCK_KEY_STAT_URL.replace('{ticker}', ticker).replace('{stat}', stat)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns the analyst price target for specified company
IEX_STOCK_PRICE_TARGET_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/price-target'
def price_target(ticker, format=None):
    url = IEX_STOCK_PRICE_TARGET_URL.replace('{ticker}', ticker)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns dividend information for specified company
IEX_STOCK_DIVIDENDS_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/dividends/{range}'
def dividends(ticker, range, format=None):
    url = IEX_STOCK_DIVIDENDS_URL.replace('{ticker}', ticker).replace('{range}', range)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns relevant stocks, similar to peers (true/false specifies whether it is the peer list)
IEX_STOCK_RELEVANT_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/relevant'
def relevant(ticker, format=None):
    url = IEX_STOCK_RELEVANT_URL.replace('{ticker}')
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns IB analyst recommendations
IEX_STOCK_RECOMENDATION_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/recommendation-trends'
def recommendation_trends(ticker, format=None):
    url = IEX_STOCK_RECOMENDATION_URL.replace('{ticker}', ticker)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns earnings estimates for the specified company
IEX_STOCK_ESTIMATES_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/estimates'
def analyst_estimates(ticker, format=None):
    url = IEX_STOCK_ESTIMATES_URL.replace('{ticker}', ticker)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

#Returns 10 most recent news items for specified company
IEX_STOCK_NEWS_URL = IEXCLOUD_STOCK_BASE_URL + 'stock/{ticker}/news'
def news(ticker, format=None):
    url = IEX_STOCK_NEWS_URL.replace('{ticker}', ticker)
    result = requests.get(append_token(url))
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result
