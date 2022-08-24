from ._common import *

options = {
"aggregates" : "/v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{from}/{to}",
"daily open/close" : "/v1/open-close/{options_ticker}/{date}",
"previous close" : "/v2/aggs/ticker/{options_ticker}/prev",
"trades" : "/v3/trades/{options_ticker}",
"last trade" : "/v2/last/trade/{options_ticker}",
"quotes" : "/v3/quotes/{options_ticker}",
"snapshot options" : "/v3/snapshot/options/{underlyingAsset}/{optionContract}"
}

options_reference = {
"options contract" : "/v3/reference/options/contracts/{options_ticker}",
"options contracts" : "/v3/reference/options/contracts",
}


def aggregates(options_ticker, multiplier, timespan, from_date, to_date, external=False, **query_params):
    """
    :return: Get aggregate bars for an option contract over a given date range in custom time window sizes.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
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
    URL_EXTENSION = F"/v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def daily_open_close(options_ticker, date, external=False, **query_params):
    """
    :return: Get the open, close and afterhours prices of an options contract on a certain date.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
    :param date: The beginning date for the aggregate window.
    :type date: required, string, date ex. '2021-07-22'
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v1/open-close/{options_ticker}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def previous_close(options_ticker, external=False, **query_params):
    """
    :return: Get the previous day's open, high, low, and close (OHLC) for the specified option contract.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param adjusted: Whether or not the results are adjusted for splits. Set this to false to get results that are NOT adjusted for splits.
    :type adjusted: optional, boolean, default True
    """
    URL_EXTENSION = F"/v2/aggs/ticker/{options_ticker}/prev"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def trades(options_ticker, external=False, **query_params):
    """
    :return: Get trades for an options ticker symbol in a given time range.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
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
    URL_EXTENSION = F"/v3/trades/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def last_trade(options_ticker, external=False, **query_params):
    """
    :return: Get the most recent trade for a given options contract.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v2/last/trade/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes(options_ticker, external=False, **query_params):
    """
    :return: Get quotes for an options ticker symbol in a given time range.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
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
    URL_EXTENSION = F"/v3/quotes/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_options(underlying_asset, option_contract, external=False, **query_params):
    """
    :return: Get the snapshot of an option contract for a stock equity.

    :param underlying_asset: The underlying ticker symbol of the option contract.
    :type underlying_asset: required, string
    :param option_contract: The option contract identifier.
    :type option_contract: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v3/snapshot/options/{underlying_asset}/{option_contract}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


def options_contract(options_ticker, external=False, **query_params):
    """
    :return: Get an options contract.

    :param options_ticker: The ticker symbol of the options contract.
    :type options_ticker: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param as_of: Specify a point in time for the contract as of this date with format YYYY-MM-DD
    :type as_of: optional, string, date ex. '2021-07-22', default is today
    """
    URL_EXTENSION = F"/v3/reference/options/contracts/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def options_contracts(external=False, **query_params):
    """
    :return: Query for historical options contracts. This provides both active and expired options contracts.

    :param underlying_asset: The underlying ticker symbol of the option contract.
    :type underlying_asset: required, string
    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param contract_type: Query by the type of contract.
    :type contract_type: optional, string
    :param expiration_date: Query by contract expiration with date format YYYY-MM-DD.
    :type expiration_date: optional, string, date ex. '2021-07-22'
    :param as_of: Specify a point in time for the contract as of this date with format YYYY-MM-DD
    :type as_of: optional, string, date ex. '2021-07-22', default is today
    :param strike_price: Query by strike price of a contract.
    :type strike_price: optional, float
    :param expired: Query for expired contracts
    :type expired: optional, boolean, default false
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v3/reference/options/contracts"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
