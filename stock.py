import requests
import os

IEXCLOUD_STOCK_BASE_URL = 'https://cloud.iexapis.com/beta/stock/'

def append_token(url):
    token = os.getenv('IEX_TOKEN')
    return "{}?token={}".format(url, token)


IEX_STOCK_CHART_URL = IEXCLOUD_STOCK_BASE_URL + '{ticker}/chart/{range}/{date}'
def chart(ticker, range, date="", format=None):
    url = IEX_STOCK_CHART_URL.replace('{ticker}', ticker).replace('{range}', range).replace('{date}', date)
    result = requests.get(append_token(url))
    print(append_token(url))
    print(result)
    result = result.json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

IEX_STOCK_FINANCIALS_URL = IEXCLOUD_STOCK_BASE_URL + '{ticker}/financials?period={period}'
def financials(ticker, period, format=None):
    url = IEX_STOCK_FINANCIALS_URL.replace("{ticker}", ticker).replace("{period}", period)
    result = requests.get(append_token(url)).json()

    if format == 'pandas':
        # Do your pandas formatting here
        pass

    if format == 'numpy':
        #do your numpy formatting here
        pass

    return result

print(chart('aapl', '5Y'))
