import requests
import xmltodict
import os

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%204%20and%20year(NEW_DATE)%20eq%202019'

#Formatting of XML to Python Dict
curve = requests.get(GOV_YIELD_URL)
curve = xmltodict.parse(curve.content)

#Definitions for various datapoints
#This will be based around retrieving the n last dates or average of n days.
feed = curve['feed']
entry = feed['entry']
content = entry[0]['content']['m:properties']

#Very verbose but makes it easy to use values in other contexts
date = entry[0]['content']['m:properties']['d:NEW_DATE']['#text']
one_month_yield = content['d:BC_1MONTH']['#text']
two_month_yield = content['d:BC_2MONTH']['#text']
three_month_yield = content['d:BC_3MONTH']['#text']
six_month_yield = content['d:BC_6MONTH']['#text']
one_year_yield = content['d:BC_1YEAR']['#text']
two_year_yield = content['d:BC_2YEAR']['#text']
three_year_yield = content['d:BC_3YEAR']['#text']
five_year_yield = content['d:BC_5YEAR']['#text']
ten_year_yield = content['d:BC_10YEAR']['#text']
twenty_year_yield = content['d:BC_20YEAR']['#text']
thirty_year_yield = content['d:BC_30YEAR']['#text']

#Dict that contains the whole yield curve so there is no need to bring in each rate.
yield_curve_values = {
        'Date' : date,
        '1 Month' : one_month_yield,
        '2 Month' : two_month_yield,
        '3 Month' : three_month_yield,
        '6 Month' : six_month_yield,
        '1 Year' : one_year_yield,
        '2 Year' : two_year_yield,
        '3 Year' : three_year_yield,
        '5 Year' : five_year_yield,
        '10 Year' : ten_year_yield,
        '20 Year' : twenty_year_yield,
        '30 Year' : thirty_year_yield,
    }

print(yield_curve_values)
