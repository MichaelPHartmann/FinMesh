from datetime import date

import stock

## TODO ##
# Add forex class
# Add premium endpoints to main IEXClass
# Add market data class

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

    def convert_listofdict_csv(self, json_doc, dictname):
        header = []
        for key in json_doc[0].keys():
            header.append(key)
        with open(self.csvfile_base.replace('%s', dictname), 'w+') as f:
            f.write(','.join(header))
            for entry in json_doc:
                for value in entry.values():
                    f.write(str(value) + ',')
                f.write('\n')

    def convert_singledict_csv(self, json_dict, dictname, orientation='horizontal'):
        if orientation == 'horizontal':
            header = []
            values = []
            for key, value in json_dict.items():
                header.append(key)
                values.append(value)
            with open(self.csvfile_base.replace('%s', dictname), 'w+') as f:
                f.write(','.join(header))
                f.write(','.join(map(str, values)))
        elif orientation == 'vertical':
            with open(self.csvfile_base.replace('%s', dictname), 'w+') as f:
                for key, value in json_dict.items():
                    f.write(str(key) + ',' + str(value) + '\n')

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
        # HORIZONTAL
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
        # HORIZONTAL
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
        # HORIZONTAL
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

    ### IEX FUNCTIONS ###

    def get_advanced_stats(self, output_csv=False):
        """3,005 credits per symbol requested.
        Returns a buffed version of key stats with selected financial data and more. Includes all data points from 'key stats'.
        CSV is formatted horizontally with keys in the first row.
        Sets class attribute 'advanced_stats'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.advanced_stats(self.ticker)
        self.advanced_stats = result
        if output_csv:
            convert_singledict_csv(result, 'advanced_stats', orientation='vertical')
        return result

    def get_book(self, output_csv=False):
        """1 credit per symbol requested.
        Returns quote, bid, ask, etc. data for the requested symbol.
        Real time data available.
        CSV is formatted horizontally with keys in the first row.
        Sets class attribute 'book'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.book(self.ticker)
        self.book = result
        if output_csv:
            convert_singledict_csv(result, 'book', orientation='vertical')
        return result

    def get_company(self, output_csv=False):
        """1 credit per symbol requested.
        Returns general information on the company requested.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'company'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.company(self.ticker)
        self.company = result
        if output_csv:
            convert_singledict_csv(result, 'company', orientation='vertical')
        return result

    def get_delayed_quote(self, output_csv=False):
        """1 credit per symbol requested.
        Returns 15 minute delayed quote for the requested symbol.
        CSV is formatted horizontally with keys in the first row.
        Sets class attribute 'delayed_quote'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.delayed_quote(self.ticker)
        self.delayed_quote = result
        if output_csv:
            convert_singledict_csv(result, 'delayed_quote', orientation='vertical')
        return result

    def get_dividends(self, output_csv=False):
        """10 credits per symbol requested.
        Returns basic dividend information for the requested symbol.
        CSV is formatted horizontally with keys in the first row.
        Sets class attribute 'dividends'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.dividends(self.ticker)
        self.dividends = result
        if output_csv:
            convert_singledict_csv(result, 'dividends', orientation='vertical')
        return result

    def get_basic_financials(self, output_csv=False):
        """5000 credits per symbol requested.
        Returns basic financial data from the requested company.
        Note that fetching all three full financial statements has the same credit cost as this endpoint.
        Sets class attribute 'basic_financials'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.financials(self.ticker)
        self.basic_financials = result
        if output_csv:
            convert_financial_json_csv(result, 'basic_financials')
        return result

    def get_fund_ownership(self, output_csv=False):
        """10,000 credits per symbol requested.
        Returns the 10 largest institutional holders of the requested company.
        Sets class attribute 'fund_ownership'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.fund_ownership(self.ticker)
        self.fund_ownership = result
        if output_csv:
            convert_listofdict_csv(result, 'fund_ownership')
        return result

    def get_insider_roster(self, output_csv):
        """5,000 credits per symbol requested.
        Returns the top 10 insiders, with the most recent information.
        Sets class attribute 'insider_roster'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.insider_roster(self.ticker)
        self.insider_roster = result
        if output_csv:
            convert_listofdict_csv(result, 'insider_roster')
        return result

    def get_insider_transactions(self, output_csv):
        """50 credits per transaction per symbol requested.
        Returns insider transactions with the most recent information.
        Sets class attribute 'insider_transactions'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.insider_transactions(self.ticker)
        self.insider_transactions = result
        if output_csv:
            convert_listofdict_csv(result, 'insider_transactions')
        return result

    def get_intitutional_ownership(self, output_csv=False):
        """10,000 credits per symbol requested
        Returns the 10 largest instituional owners for the requested stock. This is defined as explicitly buy or sell-side only.
        Sets class attribute 'institutional_ownership'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.institutional_ownership(self.ticker)
        self.institutional_ownership = reuslt
        if output_csv:
            convert_listofdict_csv(result, 'institutional_ownership')
        return result

    def get_key_stats(self, stat=None, output_csv=False):
        """5 credits per symbol requested, 1 credit per stat per symbol requested.
        Returns important stats for the requested company.
        Sets class attribute 'key_stats'.
        CSV is formatted vertically with keys in the first column
        Parameters:
        stat -> String. If you would like to querie one single stat, you can enter that here.
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.key_stats(self.ticker, stat=stat)
        self.key_stats = result
        if output_csv:
            convert_singledict_csv(result, 'key_stats', orientation='vertical')
        return result

    def get_largest_trades(self, output_csv=False):
        """1 credit per trade per symbol requested.
        This returns 15 minute delayed, last sale eligible trades.
        Sets class attribute 'largest_trades'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.largest_trades(self.ticker)
        self.largest_trades = result
        if output_csv:
            convert_listofdict_csv(result, 'largets_trades')
        return result

    def get_logo(self):
        """1 credit per symbol requested
        Returns a Google APIs link (bare url string) to the logo for the requested stock.
        Sets class attribute 'logo'.
        """
        result = stock.logo(self.ticker)['url']
        self.logo = result
        return result

    def get_news(self,last=10, output_csv=False):
        """1 credit per news article per symbol requested.
        Provides intraday news from over 3,000 global news sources including major publications, regional media, and social.
        Sets class attribute 'news'.
        Parameters ->
        last -> Integer. Number of article to return. Min = 1 Max = 50 Defualt = 10
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.news(self.ticker, last=last)
        self.news = result
        if output_csv:
            convert_listofdict_csv(result, 'news')
        return result

    def get_ohlc(self, output_csv=False):
        """2 credits per symbol requested.
        Returns the official open and close for a give symbol.
        Sets class attribute 'ohlc'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.ohlc(self.ticker)
        self.ohlc = result
        if output_csv:
            with open(self.csvfile_base.replace('%s', 'ohlc'), 'w+') as f:
                f.write(result[0])
                for key, value in result[0].items():
                    f.write(key + ',' + str(value) + '\n')
                f.write(result[1])
                for key, value in result[1].items():
                    f.write(key + ',' + str(value) + '\n')
                for key,value in result[2:].items():
                    f.write(key + ',' + str(value) + '\n')
        return result

    def get_peers(self):
        """500 credits per symbol requested.
        Returns a list of peer company's tickers in Python list form.
        Sets class attribute 'peers'.
        """
        result = stock.peers(self.ticker)
        self.peers = result
        return result

    def get_quote(self, output_csv=False):
        """1 credit per symbol requested.
        Returns quote data for the requested symbol.
        CSV is formatted vertically with keys in the first column
        Sets class attribute 'quote'.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        result = stock.quote(self.ticker)
        self.quote = result
        if output_csv:
            convert_singledict_csv(result, 'quote', orientation='vertical')
        return result

class IEXMarket():
    def __init__(self):
        self.date = date.today()
        self.available_symbols = {
        'MMNRNJ':'CD Rate Non-Jumbo less than $100,000 Money market',
        'MMNRJD':'CD Rate Jumbo more than $100,000 Money market',
        'CPIAUCSL':'Consumer Price Index All Urban Consumers',
        'TERMCBCCALLNS':'Commercial bank credit card interest rate as a percent, not seasonally adjusted',
        'FEDFUNDS':'Effective federal funds rate',
        'A191RL1Q225SBEA':'Real Gross Domestic Product',
        'WIMFSL':'Institutional money funds returned as billions of dollars, seasonally adjusted',
        'IC4WSA':'Returned as a number, seasonally adjusted',
        'INDPRO':'Industrial Production Index',
        'MORTGAGE30US':'US 30-Year fixed rate mortgage average',
        'MORTGAGE15US':'US 15-Year fixed rate mortgage average',
        'MORTGAGE5US':'US 5/1-Year fixed rate mortgage average',
        'HOUST':'Total Housing Starts in thousands of units, seasonally adjusted annual rate',
        'PAYEMS':'Total nonfarm employees in thousands of persons seasonally adjusted',
        'TOTALSA':'Total Vehicle Sales in millions of units',
        'WRMFSL':'Retail money funds returned as billions of dollars, seasonally adjusted',
        'UNRATE':'Unemployment rate returned as a percent, seasonally adjusted',
        'RECPROUSM156N':'US Recession Probabilities'
        }

    def get_single_market_data(self, symbol):
        """1,000 credits per symbol requested per date.
        Returns various economic indicator values and market datapoints.
        Sets a class attribute equal to the symbol requested.
        Parameters:
        symbol -> The symbol of the economic indicator or market datapoint requested.
        A dictionary of the available datapoints available and their corrosponding symbols is class attribute 'self.available_symbols'.
        """
        result = market.economic_data(symbol)
        setattr(IEXMarket, symbol, result)
        return result

    def get_all_market_data(self, output_csv=False):
        """18,000 credits per symbol requested per day.
        Returns all available economic indicator values and market datapoints.
        Parameters:
        output_csv -> Boolean. Creates a csv file for the ouput. Default is False.
        """
        output_data = {}
        for key in self.available_symbols.keys():
            output_data.key = market.economic_data(key)
        if output_csv:
            with open(f'{self.date}_market_data.csv', 'w+') as f:
                for key, value in output_data.items():
                    f.write(str(key) + ',' + str(value) + '\n')
        return output_data
