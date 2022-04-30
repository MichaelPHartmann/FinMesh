from ._common import *

forex = {
"aggregates" : "/v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{from}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/global/market/fx/{date}",
"previous close" : "/v2/aggs/ticker/{forex_ticker}/prev",
"quotes" : "/v3/quotes/{fxTicker}",
"historic ticks" : "/v1/historic/forex/{from}/{to}/{date}",
"last pair quote" : "/v1/last_quote/currencies/{from}/{to}",
"conversion" : "/v1/conversion/{from}/{to}",
"snapshot all" : "/v2/snapshot/locale/global/markets/forex/tickers",
"snapshot gain lose" : "/v2/snapshot/locale/global/markets/forex/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/global/markets/forex/tickers/{ticker}"
}


 def aggregates(forex_ticker, multiplier, timespan, from, to, external=False, **query_params):
     URL_EXTENSION = F"/v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{from}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def grouped_daily(date, external=False, **query_params):
     URL_EXTENSION = F"/v2/aggs/grouped/locale/global/market/fx/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def previous_close(forex_ticker, external=False, **query_params):
     URL_EXTENSION = F"/v2/aggs/ticker/{forex_ticker}/prev"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def quotes(forex_ticker, external=False, **query_params):
     URL_EXTENSION = F"/v3/quotes/{forex_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def historic_ticks(from, to, date, external=False, **query_params):
     URL_EXTENSION = F"/v1/historic/forex/{from}/{to}/{date}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def last_pair_quote(from, to, external=False, **query_params):
     URL_EXTENSION = F"/v1/last_quote/currencies/{from}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def conversion(from, to, external=False, **query_params):
     URL_EXTENSION = F"/v1/conversion/{from}/{to}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

def snapshot_gain_lose(direction, external=False, **query_params):
    URL_EXTENSION = F"/v2/snapshot/locale/global/markets/forex/{direction}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def snapshot_all(external=False, **query_params):
     URL_EXTENSION = F"/v2/snapshot/locale/global/markets/forex/tickers"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()

 def snapshot_ticker(forex_ticker, external=False, **query_params):
     URL_EXTENSION = F"/v2/snapshot/locale/global/markets/forex/tickers/{forex_ticker}"
    instance = polygonCommon(URL_EXTENSION, external=external)
    if query_params:
        instance.append_query_params_to_url(query_params)
    return instance.execute()
