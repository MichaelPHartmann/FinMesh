from iex import stock

# TO-DO #
#   Advanced Stats
IEX_ADVANCED_STATS_URL = prepend_iex_url('stock') + '{symbol}/advanced-stats'
def advanced_stats(symbol, vprint=False):
    # Returns normal key stats as well as some selected financial stats and ratios
    url = replace_url_var(IEX_ADVANCED_STATS_URL, symbol=symbol)
    return get_iex_json_request(url, vprint=vprint)
advanced_stats.__doc__='Returns normal key stats as well as some selected financial stats and ratios.'

#   Financials as Reported
IEX_FINANCIALS_REPORTED_URL = prepend_iex_url('time-series') + 'reported_financials/{symbol}/{filing}'
def financials_as_reported(symbol, filing, specification=None vprint=False):
    # Returns 10-K or 10-Q filings exactly as reported to the SEC
    url = replace_url_var(IEX_FINANCIALS_REPORTED_URL, symbol=symbol, filing=filing)
    ## Needs support for specific queries of date-specific or n-last filings
    return get_iex_json_request(url, vprint=vprint)
financials_as_reported.__doc__='Returns \'10-K\' or \'10-Q\' filings exactly as reported to the SEC'

#   Intraday Prices
IEX_INTRADAY_URL = prepend_iex_url('stock') + '{symbol}/intraday-prices'
def intraday_prices(symbol, vprint=False):
    pass

#   Technical Indicators
IEX_TECHNICAL_URL = prepend_iex_url('stock') + '{symbol}/indicator/{indicator-name}'
def technical_indicators(symbol, indicator, vprint=False):
    pass
