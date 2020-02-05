"""
# This is the full URL that I break down below:
FULL_URL = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=AAPL&type=10-Q&count=40"

# These are the components of a simple search within the Edgar system:
DOMAIN = "https://www.sec.gov"
PATH = "/cgi-bin/browse-edgar"
QUERY_STRING_ACTION = "?action=getcompany"
QUERY_STRING_TICKER = "&CIK=AAPL"
QUERY_STRING_TYPE = "&type=10-Q"
QUERY_STRING_COUNT = "&count=40"

FULL_URL = "https://www.sec.gov/Archives/edgar/data/1122304/0001193125-15-118890.txt"
DOMAIN = "https://www.sec.gov"
PATH = "/Archives/edgar/data/"
CIK = "1122304"
ACCESSION_NUM = "1122304/0001193125-15-118890"
FORMAT? = ".txt"


"https://www.sec.gov/Archives/edgar/data/1318605/000156459019003165/Financial_Report.xlsx"
"""
"""
import xml.etree.ElementTree as ET
from edgar import *

TSLA = edgar_filer('TSLA')
TSLA.cik()
print("CIK is: " + TSLA.cik)
TSLA.accession_10k(3)
last_accession = TSLA.latest_10k_accession[0]
print("Last accession is: " + last_accession)
last_10k = TSLA.retrieve_xml_report(last_accession)
print(last_10k)

tree = ET.parse(last_10k)
root = tree.getroot()
print(root)
"""


import re
import time
from _common import *

with open('Tesla.txt', 'r+') as f, open('Tesla.html', 'a') as nf:
    transfer = False
    lines = f.readlines()
    for line in lines:
        status = egdar_find_html(line)
        if status == 'Start':
            transfer = True
        elif status == 'End':
            transfer = False
            nf.write(line)

        if transfer == True:
            nf.write(line)
