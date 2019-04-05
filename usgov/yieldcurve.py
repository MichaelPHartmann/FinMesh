from ..iexfinance-py import iex.stock
from ..iexfinance-py import iex.account
from ..iexfinance-py import iex._common
import pandas as pd
from xml.dom import minidom

#General get for raw json data
def raw_yield_curve():
    url = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month%28NEW_DATE%29%20eq%205%20and%20year%28NEW_DATE%29%20eq%202013'
    data = parse(url)
    print(data)
