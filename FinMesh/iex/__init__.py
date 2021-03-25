import stock

class IEXStock:
    def __init__(self, ticker, period, last):
        self.ticker = ticker
        self.period = period
        self.last = last

    def balance_sheet(self):
        result = stock.balance_sheet(self.ticker, self.period, self.last)
        self.balance_sheet = result
        return result

    def income_statement(self):
        result = stock.income_statement(self.ticker, self.period, self.last)
        self.income_statement = result
        return result

    def cash_flow_statement(self):
        result = stock.cash_flow(self.ticker, self.period, self.last)
        self.cash_flow_statement = result
        return result

    def price(self):
        result = stock.price(self.ticker)
        self.price = result
        return result
