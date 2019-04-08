import requests
import os

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month%28NEW_DATE%29%20eq%205%20and%20year%28NEW_DATE%29%20eq%202013'

#General get for raw json data in dict form
def raw_curve():
    with open(GOV_YIELD_CURVE) as curve:
        curve = xmltodict.parse(curve.read())
    return curve
