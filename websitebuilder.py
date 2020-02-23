# List of all available functions grouped by package and sub-package

# IEX - STOCK
iex_stock_functions = {
'balance_sheet':'Returns the balance sheet fincancial statement for the requested stock.',
'book':'Returns share book information for the requested stock.',
'cash_flow':'Returns the cash flow financial statement for the requested stock.',
'collection':'Returns quotes for stocks in the requested collection type.',
'company':'Returns company data such as website, address, and description for the requested stock.',
'delayed_quote':'Returns a 15-minute delayed market quote for the requested stock.',
'dividends':'Returns dividend information for a requested stock.',
'earnings':'Returns earnings data such as actual EPS, beat/miss, and date for the requested stock.',
'today_earnings':'Returns earnings data released today, grouped by timing and stock.',
'estimates':'Returns latest future earnings estimates for the requested stock.',
'financials':'Returns a brief overview of a company\'s financial statements.',
'fund_ownership':'Returns the largest 10 fund owners of the requested stock. This excludes explicit buy or sell-side firms.',
'historical_price':'Returns the historical price for the requested stock.',
'income_statement':'Returns the income statment financial data for the requested stock.',
'insider_roster':'Returns the 10 largest insider owners for the requested stock.',
'insider_summary':'Returns a summary of the insiders and their actions within the last 6 months for the requested stock.',
'insider_transactions':'Returns a summary of insider transactions for the requested stock.',
'institutional_ownership':'Returns the 10 largest instituional owners for the requested stock. This is defined as explicitly buy or sell-side only.',
'ipo_upcoming':'Returns a list of upcoming IPOs for the current and next month.',
'ipo_today':'Returns a list of IPOs happening today.',
'key_stats':'Returns important and key statistics for the requested stock.',
'largest_trades':'Returns a delayed list of largest trades for the requested stock.',
'market_list':'Returns the 10 largest companies in the specified list.',
'logo':'Returns a Google APIs link to the logo for the requested stock.',
'market_volume':'Returns market wide trading volume.',
'news':'Returns news item summaries for the requested stock.',
'ohlc':'Returns the most recent days open, high, low, and close data for the requested stock.',
'peers':'Returns a list of a requested stocks peers.',
'previous':'Returns the previous day\'s price data for the requested stock.',
'price':'Returns a single float value of the requested company\'s price.',
'price_target':'Returns analyst\'s price targets for the requested stock.',
'quote':'Returns price quote data for the requested stock. Fields are able to be called individually.',
'recommendation_trends':'Returns analyst recommendations for the requested stocks.',
'sector_performance':'Returns market performance for all sectors.',
'splits':'Returns a record of stock splits for the given stock.',
'volume_by_venue':'Returns trading volume for the requested stock by venue.'
}

# IEX - FOREX
iex_forex_functions = {
'forex_latest_rate':'Returns the latest exchange rate for the requested currency pair.',
'forex_conversion':'Returns a converted value according to the requested currency pair.',
'forex_historical':'Returns a list of the historical exchange rates for the requested currency pair.'
}

# USGOV - FRED
usgov_fred_functions = {
'fred_series':'Returns time series historical data for the requested FRED data.',
'geofred_series_meta':'Returns meta data for the requested FRED data.',
'geofred_regional_series':'Returns the historical, geographically organized time series data for the requested FRED data.',
'get_yield':'Returns government treasury bond yields. Organized in Python dictionary format by bond length.'
}

# EDGAR
edgarFiler_functions = {
'cik':'Sets the CIK attribute for the requested company.',
'accessions':'Returns accession numbers and documents in five forms for the desired company',
'accession_request':'Returns accession numbers for the requested document.'
}
