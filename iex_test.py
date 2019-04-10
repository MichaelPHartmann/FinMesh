import iex.account
import iex.stock
import usgov.series
import usgov.yieldcurve
#from usgov.yieldcurve import *
import dict

if __name__ == "__main__":
    import json
    print("Running developer tests...")

print(usgov.series.fred_series('GNPCA'))
