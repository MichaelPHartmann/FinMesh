import requests
import xmltodict
import os

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%204%20and%20year(NEW_DATE)%20eq%202019'

def get_yield():
    # Formatting of XML to Python Dict
    curve = requests.get(GOV_YIELD_URL)
    parse_curve = xmltodict.parse(curve.content)

    # This will be based around retrieving the n last dates or average of n days.
    feed = parse_curve['feed']
    entry = feed['entry']
    last_entry = len(entry)-1
    content = entry[last_entry]['content']['m:properties']

    # Dict that contains the whole yield curve so there is no need to bring in each rate.
    return yield_curve_values = {
            'date' : entry[last_entry]['content']['m:properties']['d:NEW_DATE']['#text'],
            '1month' : content['d:BC_1MONTH']['#text'],
            '2month' : content['d:BC_2MONTH']['#text'],
            '3month' : content['d:BC_3MONTH']['#text'],
            '6month' : content['d:BC_6MONTH']['#text'],
            '1year' : content['d:BC_1YEAR']['#text'],
            '2year' : content['d:BC_2YEAR']['#text'],
            '3year' : content['d:BC_3YEAR']['#text'],
            '5year' : content['d:BC_5YEAR']['#text'],
            '10year' : content['d:BC_10YEAR']['#text'],
            '20year' : content['d:BC_20YEAR']['#text'],
            '30year' : content['d:BC_30YEAR']['#text'],
        }
