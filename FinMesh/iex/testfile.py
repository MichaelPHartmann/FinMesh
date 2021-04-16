import __init__ as g

AAPL = g.IEXStock('AAPL')
print(AAPL.get_balance_sheet(csv='prep'))
print(AAPL.balance_sheet)
