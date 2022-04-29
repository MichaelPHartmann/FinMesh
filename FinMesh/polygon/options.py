options = {
"aggregates" : "/v2/aggs/ticker/{optionsTicker}/range/{multiplier}/{timespan}/{from}/{to}",
"daily open/close" : "/v1/open-close/{optionsTicker}/{date}",
"previous close" : "/v2/aggs/ticker/{optionsTicker}/prev",
"trades" : "/v3/trades/{optionsTicker}",
"last trade" : "/v2/last/trade/{optionsTicker}",
"quotes" : "/v3/quotes/{optionsTicker}",
"snapshot options" : "/v3/snapshot/options/{underlyingAsset}/{optionContract}"
}

options_reference = {
"options contract" : "/v3/reference/options/contracts/{options_ticker}",
"options contracts" : "/v3/reference/options/contracts",
}



def aggregates():
    pass

def daily_open_close():
    pass

def previous_close():
    pass

def trades():
    pass

def last_trade():
    pass

def quotes():
    pass

def snapshot_options():
    pass


def options_contract():
    pass

def options_contracts():
    pass
