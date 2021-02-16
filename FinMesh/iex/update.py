from iex import stock

ticker = 'FARM'

# TO-DO #
# Advanced Stats
# Charts
# Extended Hours Quote
# Financials as Reported
# Intraday Prices
# Open/Close Prices
# Real-Time Quote
# SEC Filings
# Technical Indicators



## Test of possibly deprecated endpoints ##

print(stock.collection())
print(stock.earnings(ticker))
print(stock.today_earnings())
print(stock.estimates(ticker))
print(stock.ipo_upcoming())
print(stock.ipo_today())
print(stock.market_volume())
print(stock.peers(ticker))
print(stock.previous(ticker))
print(stock.recommendation_trends(ticker))
print(stock.sector_performance())
