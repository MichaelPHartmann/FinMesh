from iex import stock

# TO-DO #
#   Advanced Stats
IEX_ADVANCED_STATS_URL = prepend_iex_url('stock') + '{symbol}/advanced-stats'
def advanced_stats(symbol, vprint=False):
    pass

#   Financials as Reported
IEX_FINANCIALS_REPORTED_URL = prepend_iex_url('time-series') + 'reported_financials/{symbol}/{filing}'
def financials_as_reported(symbol, filing, vprint=False):
    pass

#   Intraday Prices
IEX_INTRADAY_URL = prepend_iex_url('stock') + '{symbol}/intraday-prices'
def intraday_prices(symbol, vprint=False):
    pass

#   Technical Indicators
IEX_TECHNICAL_URL = prepend_iex_url('stock') + '{symbol}/indicator/{indicator-name}'
def technical_indicators(symbol, indicator, vprint=False):
    pass
