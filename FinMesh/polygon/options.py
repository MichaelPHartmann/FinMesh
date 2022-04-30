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


def aggregates(options_ticker, multiplier, timespan, from, to, external=False, **query_params):
    URL_EXTENSION = F"/v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{from}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def daily_open_close(options_ticker, date, external=False, **query_params):
    URL_EXTENSION = F"/v1/open-close/{options_ticker}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def previous_close(options_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v2/aggs/ticker/{options_ticker}/prev"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def trades(options_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/trades/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def last_trade(options_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v2/last/trade/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def quotes(options_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/quotes/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_options(underlying_asset, option_contract, external=False, **query_params):
    URL_EXTENSION = F"/v3/snapshot/options/{underlying_asset}/{option_contract}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()


def options_contract(options_ticker, external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/options/contracts/{options_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def options_contracts(external=False, **query_params):
    URL_EXTENSION = F"/v3/reference/options/contracts"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
