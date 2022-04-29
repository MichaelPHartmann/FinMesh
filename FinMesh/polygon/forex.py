forex = {
"aggregates" : "/v2/aggs/ticker/{forexTicker}/range/{multiplier}/{timespan}/{from}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/global/market/fx/{date}",
"previous close" : "/v2/aggs/ticker/{forexTicker}/prev",
"quotes" : "/v3/quotes/{fxTicker}",
"historic ticks" : "/v1/historic/forex/{from}/{to}/{date}",
"last pair quote" : "/v1/last_quote/currencies/{from}/{to}",
"conversion" : "/v1/conversion/{from}/{to}",
"snapshot all" : "/v2/snapshot/locale/global/markets/forex/tickers",
"snapshot gain lose" : "/v2/snapshot/locale/global/markets/forex/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/global/markets/forex/tickers/{ticker}"
}

 def aggregates():
     pass

 def grouped_daily():
     pass

 def previous_close():
     pass

 def quotes():
     pass

 def historic_ticks():
     pass

 def last_pair_quote():
     pass

 def conversion():
     pass

def snapshot_gain_lose():
    pass

 def snapshot_all():
     pass

 def snapshot_ticker():
     pass
