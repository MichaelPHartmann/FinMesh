import stock

class Stock:
    def __init__(self, ticker, period='quarter', last=1, output_csv=False, autopopulate=False):
        self.ticker = ticker
        self.period = period
        self.last = last
        self.csvfile_base = f'{ticker}_%s.csv'

        if autopopulate:
            basic_information()
            price_information()

    def basic_information():
        # 6 credits per symbol requested
        # Could be pared down to 5 credits but not economical
        company_request = stock.company(self.ticker)
        self.company_name = company_request['companyName']
        self.industry = company_request['industry']
        key_stat_request = stock.key_stats(self.ticker)
        self.market_cap = key_stat_request['marketcap']
        self.pe_ratio = key_stat_request['peRatio']
        self.beta = key_stat_request['beta']

    def price_information():
        # 6 credits pers symbol requested
        key_stat_request = stock.key_stats(self.ticker)
        self.week52_high = key_stat_request['week52high']
        self.week52_low = key_stat_request['week52low']
        self.moving_average_200 = key_stat_request['day200MovingAvg']
        self.moving_average_50 = key_stat_request['day50MovingAvg']
        self.price = stock.price(self.ticker)

    def balance_sheet(self, output_csv=False):
        # 3,000 credits per symbol requested
        result = stock.balance_sheet(self.ticker, self.period, self.last)
        self.balance_sheet = result
        return result

    def income_statement(self, output_csv=False):
        # 1,000 credits per symbol requested
        result = stock.income_statement(self.ticker, self.period, self.last)
        self.income_statement = result
        return result

    def cash_flow_statement(self, output_csv=False):
        # 1,000 credits per symbol requested
        result = stock.cash_flow(self.ticker, self.period, self.last)
        self.cash_flow_statement = result
        return result

    def get_financial_statements(self):
        income_statement()
        balance_sheet()
        cash_flow_statement()

    def price(self):
        # 1 credit per symbol requested
        result = stock.price(self.ticker)
        self.price = result
        return result

    def convert_dict_csv(self, json, statement):
        header = []
        incomeStatement = 'income'
        balanceSheet = 'balancesheet'
        cashFlow = 'cashflow'
        for key, value in json[statement][0]:
            header.append(key)
        with open(self.csvfile_base.replace('%s', statement), 'w+') as f:
            f.write(header.join(','))
            f.write('\n')
            for period in range(len(json[statement])):
                for key, value in json[statement][period]:
                    f.write(str(value) + ',')
                f.write('\n')

if __name__ == '__main__':
    print(stock.cash_flow('AAPL',last=1))
