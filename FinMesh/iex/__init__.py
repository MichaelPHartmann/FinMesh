import stock

class IEXStock:
    def __init__(self, ticker, period='quarter', last=1, autopopulate=False):
        self.ticker = ticker
        self.period = period
        self.last = last
        if autopopulate:
            basic_information()
            price_information()

    def basic_information():
        company_request = stock.company(self.ticker)
        self.company_name = company_request['companyName']
        self.industry = company_request['industry']
        key_stat_request = stock.key_stats(self.ticker)
        self.market_cap = key_stat_request['marketcap']
        self.pe_ratio = key_stat_request['peRatio']
        self.beta = key_stat_request['beta']

    def price_information():
        key_stat_request = stock.key_stats(self.ticker)
        self.week52_high = key_stat_request['week52high']
        self.week52_low = key_stat_request['week52low']
        self.moving_average_200 = key_stat_request['day200MovingAvg']
        self.moving average_50 = key_stat_request['day50MovingAvg']
        self.price = stock.price(self.ticker)

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
