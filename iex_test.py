import iex.account
import iex.stock
import usgov.yieldcurve
import dict

if __name__ == "__main__":
    import json
    print("Running developer tests...")

raw = usgov.yieldcurve.raw_yield_curve()
print(raw.keys())

print()
