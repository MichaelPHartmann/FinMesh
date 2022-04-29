stocks = {
"aggregates" : "/v2/aggs/ticker/{stockTicker}/range/{multiplier}/{timespan}/{from}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/us/market/stocks/{date}",
"daily open/close" : "/v1/open-close/{stockTicker}/{date}",
"previous close" : "/v2/aggs/ticker/{stockTicker}/prev",
"trades v3" : "/v3/trades/{stockTicker}",
"trades" : "/v2/ticks/stocks/trades/{stockTicker}/{date}",
"last trade" : "/v2/last/trade/{stockTicker}",
"quotes v3" : "/v3/quotes/{stockTicker}",
"quotes v2" : "/v2/ticks/stocks/nbbo/{stockTicker}/{date}",
"last quote" : "/v2/last/nbbo/{stockTicker}",
"snapshot all" : "/v2/snapshot/locale/us/markets/stocks/tickers",
"snapshot gain/lose" : "/v2/snapshot/locale/us/markets/stocks/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/us/markets/stocks/tickers/{stockTicker}"
}

stocks_reference = {
"ticker details" : "/v3/reference/tickers/{stockTicker}",
"stock splits v3" : "/v3/reference/splits",
"dividends v3" : "/v3/reference/dividends",
"financials" : "/vX/reference/financials",
}


def aggregates():
    pass
    
def grouped_daily():
    pass
    
def daily_open_close():
    pass
    
def previous_close():
    pass
    
def trades_v3():
    pass
    
def trades():
    pass
    
def last_trade():
    pass
    
def quotes_v3():
    pass
    
def quotes_v2():
    pass
    
def last_quote():
    pass
    
def snapshot_all():
    pass
    
def snapshot_gain_lose():
    pass
    
def snapshot_ticker():
    pass
    

def ticker_details():
    pass
    
def stock_splits_v3():
    pass
    
def dividends_v3():
    pass
    
def financials():
    pass
    
