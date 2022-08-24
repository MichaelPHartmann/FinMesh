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


def aggregates(stock_ticker, multiplier, timespan, from_date, to_date, external=False, **query_params):
    """
    :return: Get aggregate bars for a stock over a given date range in custom time window sizes.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param multiplier: The size of the timespan multiplier.
    :type multiplier: required, integer
    :param timespan: The size of the time window.
    :type timespan: required, string, [minute, hour, day, week, month, quarter, year]
    :param from: The start of the aggregate time window.
    :type from: required, string, date ex. '2021-07-22'
    :param to: The end of the aggregate time window.
    :type to: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    :param sort: Sort the results by timestamp.
    :type sort: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    """
    URL_EXTENSION = F"/v2/aggs/ticker/{stock_ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def grouped_daily(date, external=False, **query_params):
    """
    :return: Get the daily open, high, low, and close (OHLC) for the entire stocks/equities markets.

    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v2/aggs/grouped/locale/us/market/stocks/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def daily_open_close(stock_ticker, date, external=False, **query_params):
    """
    :return: Get the open, close and afterhours prices of a stock symbol on a certain date.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v1/open-close/{stock_ticker}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def previous_close(stock_ticker, external=False, **query_params):
    """
    :return: Get the previous day's open, high, low, and close (OHLC) for the specified stock ticker.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v2/aggs/ticker/{stock_ticker}/prev"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def trades_v3(stock_ticker, external=False, **query_params):
    """
    :return: Get trades for a ticker symbol in a given time range.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
    :type timestamp: optional, string, date or nanosecond timestamp
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v3/trades/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def trades(stock_ticker, date, external=False, **query_params):
    """
    :return: Get trades for a given ticker symbol on a specified date.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
    :type timestamp: optional, string, date or nanosecond timestamp
    :param timestamp_limit: The maximum timestamps allowed in the results.
    :type timestamp_limit: optional, integer
    :param reverse: Reverse the order of the results.
    :type reverse: optional, boolean
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    """
    URL_EXTENSION = F"/v2/ticks/stocks/trades/{stock_ticker}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


def last_trade(stock_ticker, external=False, **query_params):
    """
    :return: Get the most recent trade for a given stock.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    """
    URL_EXTENSION = F"/v2/last/trade/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes_v3(stock_ticker, external=False, **query_params):
    """
    :return: Get NBBO quotes for a ticker symbol in a given time range.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
    :type timestamp: optional, string, date or nanosecond timestamp
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v3/quotes/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes_v2(stock_ticker, external=False, **query_params):
    """
    :return: Get NBBO quotes for a given ticker symbol on a specified date.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
    :type timestamp: optional, string, date or nanosecond timestamp
    :param timestamp_limit: The maximum timestamps allowed in the results.
    :type timestamp_limit: optional, integer
    :param reverse: Reverse the order of the results.
    :type reverse: optional, boolean
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    """
    URL_EXTENSION = F"/v3/quotes/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def last_quote(stock_ticker, external=False, **query_params):
    """
    :return: Get the most recent NBBO (Quote) tick for a given stock.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v2/last/nbbo/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_all(external=False, **query_params):
    """
    :return: Get the most up-to-date market data for all traded stock symbols.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param tickers: A comma separated list of tickers to get snapshots for.
    :type tickers: optional, string, list of tickers
    """
    URL_EXTENSION = F"/v2/snapshot/locale/us/markets/stocks/tickers"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_gain_lose(direction, external=False, **query_params):
    """
    :return: Get the most up-to-date market data for the current top 20 gainers or losers of the day in the stocks/equities markets.

    :param direction: The direction of the snapshot results to return.
    :type direction: required, string, [gainers, losers]
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v2/snapshot/locale/us/markets/stocks/{direction}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_ticker(stock_ticker, external=False, **query_params):
    """
    :return: Get the most up-to-date market data for a single traded stock ticker.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v2/snapshot/locale/us/markets/stocks/tickers/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def ticker_details(stock_ticker, external=False, **query_params):
    """
    :return: Get a single ticker supported by Polygon.io. This response will have detailed information about the ticker and the company behind it.

    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param date: The beginning date for the aggregate window.
    :type date: optional, string, date ex. '2021-07-22'
    """
    URL_EXTENSION = F"/v3/reference/tickers/{stock_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def stock_splits_v3(external=False, **query_params):
    """
    :return: Get a list of historical stock splits, including the ticker symbol, the execution date, and the factors of the split ratio.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param execution_date: Query by execution date.
    :type execution_date: optional, string, date ex. '2021-07-22'
    :param reverse_split:Query for reverse splits only.
    :type reverse_split: optional, boolean
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v3/reference/splits"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def dividends_v3(external=False, **query_params):
    """
    :return: Get a list of historical cash dividends, including the ticker symbol, declaration date, ex-dividend date, record date, pay date, frequency, and amount.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param ex_dividend_date: Query by ex-dividend date with the format YYYY-MM-DD.
    :type ex_dividend_date: optional, string, date ex. '2021-07-22'
    :param record_date: Query by record date with the format YYYY-MM-DD.
    :type record_date: optional, string, date ex. '2021-07-22'
    :param declaration_date: Query by declaration date with the format YYYY-MM-DD.
    :type declaration_date: optional, string, date ex. '2021-07-22'
    :param pay_date: Query by pay date with the format YYYY-MM-DD.
    :type pay_date: optional, string, date ex. '2021-07-22'
    :param frequency: Query by the number of times per year the dividend is paid out.
    :type frequency: optional, integer, eg. [0,1,2,4,12]
    :param cash_amount: Query by the cash amount of the dividend.
    :type cash_amount: optional, float
    :param dividend_type: Query by the type of dividend.
    :type dividend_type: optional, string, Consistent Dividends = CD, Special Cash Dividends = [SC]
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v3/reference/dividends"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def financials(external=False, **query_params):
    """
    This API is experimental.
    :return: Get historical financial data for a stock ticker.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param stock_ticker: The ticker symbol of the stock.
    :type stock_ticker: required, string
    :param cik:
    :type cik:
    :param company_name:
    :type company_name:
    :param sic:
    :type sic:
    :param :
    :type :
    :param :
    :type :
    :param :
    :type :
    :param :
    :type :
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/vX/reference/financials"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
