import __init__ as b

AAPL = b.IEXStock('AAPL')
print(AAPL.get_company(output_csv=True))
