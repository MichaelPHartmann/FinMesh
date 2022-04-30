from ._common import *

stocks = {
"aggregates" : "/v2/aggs/ticker/{stock_ticker}/range/{multiplier}/{timespan}/{from}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/us/market/stocks/{date}",
"daily open/close" : "/v1/open-close/{stock_ticker}/{date}",
"previous close" : "/v2/aggs/ticker/{stock_ticker}/prev",
"trades v3" : "/v3/trades/{stock_ticker}",
"trades" : "/v2/ticks/stocks/trades/{stock_ticker}/{date}",
"last trade" : "/v2/last/trade/{stock_ticker}",
"quotes v3" : "/v3/quotes/{stock_ticker}",
"quotes v2" : "/v2/ticks/stocks/nbbo/{stock_ticker}/{date}",
"last quote" : "/v2/last/nbbo/{stock_ticker}",
"snapshot all" : "/v2/snapshot/locale/us/markets/stocks/tickers",
"snapshot gain/lose" : "/v2/snapshot/locale/us/markets/stocks/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/us/markets/stocks/tickers/{stock_ticker}"
}

stocks_reference = {
"ticker details" : "/v3/reference/tickers/{stock_ticker}",
"stock splits v3" : "/v3/reference/splits",
"dividends v3" : "/v3/reference/dividends",
"financials" : "/vX/reference/financials",
}


def aggregates(stock_ticker, multiplier, timespan, from, to, external=False, **query_params):
    URL_EXTENSION = F"/v2/aggs/ticker/{stock_ticker}/range/{multiplier}/{timespan}/{from}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def grouped_daily(date, external=False, **query_params):
    URL_EXTENSION = F"/v2/aggs/grouped/locale/us/market/stocks/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def daily_open_close(stock_ticker, date, external=False, **query_params):
    URL_EXTENSION = F"/v1/open-close/{stock_ticker}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def previous_close(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v2/aggs/ticker/{stock_ticker}/prev"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def trades_v3(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/trades/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def trades(stock_ticker, date, external=False, **query_params):
    URL_EXTENSION = F"/v2/ticks/stocks/trades/{stock_ticker}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


def last_trade(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v2/last/trade/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes_v3(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/quotes/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes_v2(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/quotes/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def last_quote(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v2/last/nbbo/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_all(external=False, **query_params):
    URL_EXTENSION = F"/v2/snapshot/locale/us/markets/stocks/tickers"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_gain_lose(direction, external=False, **query_params):
    URL_EXTENSION = F"/v2/snapshot/locale/us/markets/stocks/{direction}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_ticker(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v2/snapshot/locale/us/markets/stocks/tickers/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def ticker_details(stock_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/tickers/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def stock_splits_v3(external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/splits"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def dividends_v3(external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/dividends"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def financials(external=False, **query_params):
    URL_EXTENSION = F"/vX/reference/financials"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
