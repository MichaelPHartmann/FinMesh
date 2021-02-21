from iex import stock

#   Financials as Reported
IEX_FINANCIALS_REPORTED_URL = prepend_iex_url('time-series') + 'reported_financials/{symbol}/{filing}'
def financials_as_reported(symbol, filing, specification=None vprint=False):
    # Returns 10-K or 10-Q filings exactly as reported to the SEC
    url = replace_url_var(IEX_FINANCIALS_REPORTED_URL, symbol=symbol, filing=filing)
    ## Needs support for specific queries of date-specific or n-last filings
    return get_iex_json_request(url, vprint=vprint)
financials_as_reported.__doc__='Returns \'10-K\' or \'10-Q\' filings exactly \as reported to the SEC. Queries based on \'last\', \'on\', \or \'from\' specifications must be entered \as directed by IEX documentation.'
