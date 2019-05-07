import iex.account
import iex.stock
import usgov.yieldcurve
import usgov.fred

if __name__ == "__main__":
    import json
    print("Running developer tests...")

print(iex.stock.quote('AAPL'))
