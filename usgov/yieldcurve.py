import requests
import xmltodict
import os

GOV_YIELD_URL = 'https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData?$filter=month(NEW_DATE)%20eq%204%20and%20year(NEW_DATE)%20eq%202019'

#Formatting of XML to Python Dict
curve = requests.get(GOV_YIELD_URL)
parse_curve = xmltodict.parse(curve.content)

#Definitions for various datapoints
#This will be based around retrieving the n last dates or average of n days.
feed = parse_curve['feed']
entry = feed['entry']
last_entry = len(entry)-1
content = entry[last_entry]['content']['m:properties']

#Very verbose but makes it easy to use values in other contexts
date = entry[last_entry]['content']['m:properties']['d:NEW_DATE']['#text']
def date():
    date = entry[last_entry]['content']['m:properties']['d:NEW_DATE']['#text']
    return date
one_month_yield = content['d:BC_1MONTH']['#text']
def one_month_yield():
    one_month_yield = content['d:BC_1MONTH']['#text']
    return one_month_yield
two_month_yield = content['d:BC_2MONTH']['#text']
def two_month_yield():
    two_month_yield = content['d:BC_2MONTH']['#text']
    return two_month_yield
three_month_yield = content['d:BC_3MONTH']['#text']
def three_month_yield():
    three_month_yield = content['d:BC_3MONTH']['#text']
    return three_month_yield
six_month_yield = content['d:BC_6MONTH']['#text']
def six_month_yield():
    six_month_yield = content['d:BC_6MONTH']['#text']
    return six_month_yield
one_year_yield = content['d:BC_1YEAR']['#text']
def one_year_yield():
    one_year_yield = content['d:BC_1YEAR']['#text']
    return one_year_yield
two_year_yield = content['d:BC_2YEAR']['#text']
def two_year_yield():
    two_year_yield = content['d:BC_2YEAR']['#text']
    return two_year_yield
three_year_yield = content['d:BC_3YEAR']['#text']
def three_year_yield():
    three_year_yield = content['d:BC_3YEAR']['#text']
    return three_year_yield
five_year_yield = content['d:BC_5YEAR']['#text']
def five_year_yield():
    five_year_yield = content['d:BC_5YEAR']['#text']
    return five_year_yield
ten_year_yield = content['d:BC_10YEAR']['#text']
def ten_year_yield():
    ten_year_yield = content['d:BC_10YEAR']['#text']
    return ten_year_yield
twenty_year_yield = content['d:BC_20YEAR']['#text']
def twenty_year_yield():
    twenty_year_yield = content['d:BC_20YEAR']['#text']
    return twenty_year_yield
thirty_year_yield = content['d:BC_30YEAR']['#text']
def thirty_year_yield():
    thirty_year_yield = content['d:BC_30YEAR']['#text']
    return thirty_year_yield

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
