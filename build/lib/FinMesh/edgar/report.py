from edgar import *

AAPL = edgarFiler('FARM')
AAPL.process_reports(5, '10-K')
