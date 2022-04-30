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
    URL_EXTENSION = F"/v3/reference/tickers"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def ticker_news(external=False, **query_params):
    URL_EXTENSION = F"/v2/reference/news"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def ticker_types(external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/tickers/types"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def market_holidays(external=False, **query_params):
    URL_EXTENSION = F"/v1/marketstatus/upcoming"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def market_status(external=False, **query_params):
    URL_EXTENSION = F"/v1/marketstatus/now"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def conditions(external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/conditions"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def exchanges(external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/exchanges"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
