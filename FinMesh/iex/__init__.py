import stock

class IEXStock:
    def __init__(self, ticker, period='quarter', last=1, autopopulate=False):
        self.ticker = ticker
        self.period = period
        self.last = last
        self.csvfile_base = f'{ticker}_%s.csv'

        if autopopulate:
            basic_information()
            price_information()

    ### HELPER FUNCTIONS ###

    def convert_financial_json_csv(self, json, statement):
        """Converts IEX JSON financial statements into csv files.

        Parameters:
        json -> The IEX JSON financial statement document
        statement -> String. Accepts ['income, balancesheet', 'cashflow']
        """
        header = []
        for key in json[statement][0].keys():
            header.append(key)
        with open(self.csvfile_base.replace('%s', statement), 'w+') as f:
            f.write(','.join(header))
            f.write('\n')
            for period in range(len(json[statement])):
                for key, value in json[statement][period].items():
                    f.write(str(value) + ',')
                f.write('\n')

    def convert_price_json_csv(self, json_doc, period):
        header = []
        for key in json_doc[0].keys():
            header.append(key)
        with open(self.csvfile_base.replace('%s', period), 'w+') as f:
            f.write(','.join(header))
            f.write('\n')
            for day in range(len(json_doc)):
                for key, value in json_doc.items():
                    f.write(str(value) + ',')
                f.write('\n')

    ### BASIC AND PRICE INFORMATION ###

    def basic_information(self):
        """6 credits per symbol requested.
        Makes requests to the company and key stat IEX endpoints.
        Sets class attributes for:
        Company name (self.company_name)
        Industry (self.industry)
        Market Capitalization (self.market_cap)
        P/E Ratio (self.pe_ratio)
        Beta (self.beta)
        """
        company_request = stock.company(self.ticker)
        self.company_name = company_request['companyName']
        self.industry = company_request['industry']
        key_stat_request = stock.key_stats(self.ticker)
        self.market_cap = key_stat_request['marketcap']
        self.pe_ratio = key_stat_request['peRatio']
        self.beta = key_stat_request['beta']

    def price_information(self):
        """6 credits per symbol requested.
        Makes requests to the key stat and price endpoints.
        Sets class attributes for:
        52 week high (week52_high), 52 week low (week52_low)
        200 day moving average (moving_average_200), 50 day moving average (moving_average_50)
        Most recent price (self.price)
        """
        key_stat_request = stock.key_stats(self.ticker)
        self.week52_high = key_stat_request['week52high']
        self.week52_low = key_stat_request['week52low']
        self.moving_average_200 = key_stat_request['day200MovingAvg']
        self.moving_average_50 = key_stat_request['day50MovingAvg']
        self.price = stock.price(self.ticker)

    def price(self):
        """1 credit per symbol requested.
        Returns the most recent price for the requested company and sets class attribute 'self.price'.
        """
        result = stock.price(self.ticker)
        self.price = result
        return result

    def get_historical_price(self, time_frame, date=None, chart_by_day=False, chart_close_only=False, output_csv=False):
        """10 credits per day requested when part of a time frame. (Full Data)
        50 credits per single day, minute data.
        Parameters:
        time_frame -> String. Determines how far back to retrieve data. Set to 'date' if only one specific day is required.
        date -> String. If 'date' is specified in time_frame, this is the date that you wish to access.
        chart_by_date -> Boolean. If a single date is requested, setting param to True only returns OHLC data instead of minutely data.
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.new_historical_price(self.ticker, period=time_frame, date=date, chart_by_day=chart_by_day, chart_close_only=chart_close_only)
        attribute_name = f"{period}_historical_price"
        setattr(IEXStock, attribute_name, result)
        if output_csv:
            convert_price_json_csv(result, time_frame)
        return result

    ### FINANCIAL STATEMENTS ###

    def get_balance_sheet(self, period=None, last=None, output_csv=False):
        """3,000 credits per symbol requested.
        Returns balance sheet data for the requested company and sets class attribute 'self.balance_sheet'.
        Parameters:
        period -> String. Accepts ['annual', 'quarterly']. Defaults to quarterly
        last -> Integer. Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.balance_sheet(self.ticker, period=period, last=last)
        self.balance_sheet = result
        if output_csv:
            convert_financial_json_csv(result, 'balancesheet')
        return result

    def get_income_statement(self, period=None, last=None, output_csv=False):
        """1,000 credits per symbol requested.
        Returns income statement data for the requested company and sets class attribute 'self.income_statement'.
        Parameters:
        period -> String. Accepts ['annual', 'quarterly']. Defaults to quarterly
        last -> Integer. Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.income_statement(self.ticker, period=period, last=last)
        self.income_statement = result
        if output_csv:
            self.convert_financial_json_csv(result, 'income')
        return result

    def get_cash_flow_statement(self, period=None, last=None, output_csv=False):
        """1,000 credits per symbol requested.
        Returns cash flow statement data for the requested company and sets class attribute 'self.cash_flow_statement'.
        Parameters:
        period -> String. Accepts ['annual', 'quarterly'], defaults to quarterly
        last -> Integer. Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.cash_flow(self.ticker, period=period, last=last)
        self.cash_flow_statement = result
        if output_csv:
            convert_financial_json_csv(result, 'cashflow')
        return result

    def get_financial_statements(self, output_csv=False):
        """5,000 credits per symbol requested.
        Simply fetches all the financial statements at once.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        income_statement(output_csv=False)
        balance_sheet(output_csv=False)
        cash_flow_statement(output_csv=False)
