from ._common import *

forex = {
"aggregates" : "/v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{from_date}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/global/market/fx/{date}",
"previous close" : "/v2/aggs/ticker/{forex_ticker}/prev",
"quotes" : "/v3/quotes/{fxTicker}",
"historic ticks" : "/v1/historic/forex/{from_date}/{to}/{date}",
"last pair quote" : "/v1/last_quote/currencies/{from_date}/{to}",
"conversion" : "/v1/conversion/{from_date}/{to}",
"snapshot all" : "/v2/snapshot/locale/global/markets/forex/tickers",
"snapshot gain lose" : "/v2/snapshot/locale/global/markets/forex/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/global/markets/forex/tickers/{ticker}"
}


def aggregates(forex_ticker, multiplier, timespan, from_date, to_date, external=False, **query_params):
    """
    :return: Get aggregate bars for a forex pair over a given date range in custom time window sizes.

    :param forex_ticker: The ticker symbol of the currency pair.
    :type forex_ticker: required, string
    :param multiplier: The size of the timespan multiplier.
    :type multiplier: required, integer
    :param timespan: The size of the time window.
    :type timespan: required, string, [minute, hour, day, week, month, quarter, year]
    :param from_date: The start of the aggregate time window.
    :type from_date: required, string, date ex. '2021-07-22'
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
    URL_EXTENSION = F"/v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def grouped_daily(date, external=False, **query_params):
    """
    :return: Get the daily open, high, low, and close (OHLC) for the entire forex markets.

    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v2/aggs/grouped/locale/global/market/fx/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def previous_close(forex_ticker, external=False, **query_params):
    """
    :return: Get the previous day's open, high, low, and close (OHLC) for the specified forex pair.

    :param forex_ticker: The ticker symbol of the currency pair.
    :type forex_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v2/aggs/ticker/{forex_ticker}/prev"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes(forex_ticker, external=False, **query_params):
    """
    :return: Get BBO quotes for a ticker symbol in a given time range.

    :param forex_ticker: The ticker symbol of the currency pair.
    :type forex_ticker: required, string
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
    URL_EXTENSION = F"/v3/quotes/{forex_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def historic_ticks(from_date, to, date, external=False, **query_params):
    """
    :return: Get historic ticks for a forex currency pair.

    :param from_date: The start of the aggregate time window.
    :type from_date: required, string, date ex. '2021-07-22'
    :param to: The end of the aggregate time window.
    :type to: required, string, date ex. '2021-07-22'
    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param offset: The timestamp offset, used for pagination. This is the offset at which to start the results.
    :type offset: optional, string, date or nanosecond timestamp
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    """
    URL_EXTENSION = F"/v1/historic/forex/{from_date}/{to}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def last_pair_quote(from_date, to, external=False, **query_params):
    """
    :return: Get the last quote tick for a forex currency pair.

    :param from_date: The start of the aggregate time window.
    :type from_date: required, string, date ex. '2021-07-22'
    :param to: The end of the aggregate time window.
    :type to: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v1/last_quote/currencies/{from_date}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def conversion(from_date, to, external=False, **query_params):
    """
    :return: Get currency conversions using the latest market conversion rates. Note than you can convert in both directions.

    :param from_date: The start of the aggregate time window.
    :type from_date: required, string, date ex. '2021-07-22'
    :param to: The end of the aggregate time window.
    :type to: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param amount: The amount to convert, with a decimal.
    :type amount: optional, integer
    :param precision: The decimal precision of the conversion. Defaults to 2 which is 2 decimal places accuracy.
    :type precision: optional, integer
    """
    URL_EXTENSION = F"/v1/conversion/{from_date}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_gain_lose(direction, external=False, **query_params):
    """
    :return: Get the current top 20 gainers or losers of the day in forex markets.

    :param direction: The direction of the snapshot results to return.
    :type direction: required, string, [gainers, losers]
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v2/snapshot/locale/global/markets/forex/{direction}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_all(external=False, **query_params):
    """
    :return: Get the current minute, day, and previous day’s aggregate, as well as the last trade and quote for all traded forex symbols.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param tickers: A comma separated list of tickers to get snapshots for.
    :type tickers: optional, string, list of tickers
    """
    URL_EXTENSION = F"/v2/snapshot/locale/global/markets/forex/tickers"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_ticker(forex_ticker, external=False, **query_params):
    """
    :return:Get the current minute, day, and previous day’s aggregate, as well as the last trade and quote for a single traded currency symbol.

    :param forex_ticker: The ticker symbol of the currency pair.
    :type forex_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v2/snapshot/locale/global/markets/forex/tickers/{forex_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
