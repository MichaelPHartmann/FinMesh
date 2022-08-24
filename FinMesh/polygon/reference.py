from ._common import *

reference = {
"tickers" : "/v3/reference/tickers",
"ticker news" : "/v2/reference/news",
"ticker types" : "/v3/reference/tickers/types",
"market holidays" : "/v1/marketstatus/upcoming",
"market status" : "/v1/marketstatus/now",
"conditions" : "/v3/reference/conditions",
"exchanges" : "/v3/reference/exchanges"
}


def tickers(external=False, **query_params):
    """
    :return: Query all ticker symbols which are supported by Polygon.io.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param ticker: The ticker for which you would like to query information for.
    :type ticker: optional, string
    :param type: The type of the ticker, Available through Polygon.io's Ticker Types API.
    :type type: optional, string, default is to query all types
    :param market: The market you would like to filter results by.
    :type market: optional, string, default is to query all markets
    :param exchange: The primary exchange of the asset in the ISO code format.
    :type exchange: optional, string, default is to query all exchanges
    :param cusip: The CUSIP code of the asset you want to search for.
    :type cusip: optional, string, default is to query all CUSIPs
    :param cik: The CIK of the asset you want to search for.
    :type cik: optional, string, default is to query all CIKs
    :param date: Specify a point in time to retrieve tickers available on that date.
    :type date: optional, string, date ex. '2021-07-22', default is most recent date
    :param search: Search for terms within the ticker and/or company name.
    :type search: optional, string
    :param active: Specify if the tickers returned should be actively traded on the queried date
    :type active: optional, boolean, default is true
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    """
    URL_EXTENSION = F"/v3/reference/tickers"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def ticker_news(external=False, **query_params):
    """
    :return: Get the most recent news articles relating to a stock ticker symbol, including a summary of the article and a link to the original source.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param ticker: The ticker for which you would like to query information for.
    :type ticker: optional, string
    :param published_utc: Return results published on, before, or after this date.
    :type published_utc: optional, string, date ex. '2021-07-22'
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v2/reference/news"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def ticker_types(external=False, **query_params):
    """
    :return: List all ticker types that Polygon.io has.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param asset_class: The asset class by which you would like to filter results.
    :type asset_class: optional, string
    :param locale: The locale by which you would like to filter results.
    :type locale: optional, string
    """
    URL_EXTENSION = F"/v3/reference/tickers/types"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def market_holidays(external=False, **query_params):
    """
    :return: Get upcoming market holidays and their open/close times.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v1/marketstatus/upcoming"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def market_status(external=False, **query_params):
    """
    :return: Get the current trading status of the exchanges and overall financial markets.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    """
    URL_EXTENSION = F"/v1/marketstatus/now"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def conditions(external=False, **query_params):
    """
    :return: List all conditions that Polygon.io uses.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param asset_class: The asset class by which you would like to filter results.
    :type asset_class: optional, string
    :param data_type: The data type by which you would like to filter results.
    :type data_type: optional, string
    :param id: Filter for conditions with a given ID.
    :type id: optional, integer
    :param sip: Filter by SIP. If the condition contains a mapping for that SIP, the condition will be returned.
    :type sip: optional, string, [CTA, UTP, OPRA]
    :param order: Order results based on the sort field.
    :type order: optional, string, [desc, asc]
    :param limit: Limits the number of base aggregates queried to create the aggregate results.
    :type limit: optional, integer, default 5000, max 50000
    :param sort: Sort field used for ordering.
    :type sort: optional, string
    """
    URL_EXTENSION = F"/v3/reference/conditions"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def exchanges(external=False, **query_params):
    """
    :return: List all exchanges that Polygon.io knows about.

    :param external: Your Polygon API key if you are not using environment variables.
    :type external: optional, string
    :param asset_class: The asset class by which you would like to filter results.
    :type asset_class: optional, string
    :param locale: The locale by which you would like to filter results.
    :type locale: optional, string
    """
    URL_EXTENSION = F"/v3/reference/exchanges"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
