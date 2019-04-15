import iex.account
import iex.stock
import usgov.yieldcurve
import usgov.fred
import dict

if __name__ == "__main__":
    import json
    print("Running developer tests...")

test = usgov.fred.geofred_series_meta('WIPCPI')

print(test)
