from datetime import date

import stock
import market

class IEXStock:
    def __init__(self, ticker, period='quarter', last=1, autopopulate=False):
        self.ticker = ticker
        self.period = period
        self.last = last
        self.csvfile_base = f'{ticker}_%s.csv'
        self.date = date.today()

        if autopopulate:
            basic_information()
            price_information()

    #  _  _     _                 ___             _   _
    # | || |___| |_ __  ___ _ _  | __|  _ _ _  __| |_(_)___ _ _  ___
    # | __ / -_) | '_ \/ -_) '_| | _| || | ' \/ _|  _| / _ \ ' \(_-<
    # |_||_\___|_| .__/\___|_|   |_| \_,_|_||_\__|\__|_\___/_||_/__/
    #            |_|


    # NEW
    def prep_financial_json_csv(self, json, statement):
        """Prepares a JSON document containing a financial data for writing to a CSV file.
        Parameters:
        json_doc -> a raw json document containing financial data
        """
        doc_to_write = ''
        header = []
        for key in json[statement][0].keys():
            header.append(key)
        doc_to_write += (','.join(header))
        doc_to_write += ('\n')
        for period in range(len(json[statement])):
            for key, value in json[statement][period].items():
                doc_to_write += (str(value) + ',')
            doc_to_write += ('\n')
        return doc_to_write

    # NEW
    def prep_price_json_csv(self, json_doc):
        """Prepares a JSON document containing a stock price data for writing to a CSV file.
        Parameters:
        json_doc -> a raw json document containing price data
        """
        doc_to_write = ''
        header = []
        for key in json_doc[0].keys():
            header.append(key)
        doc_to_write += (','.join(header))
        doc_to_write += ('\n')
        for day in range(len(json_doc)):
            for key, value in json_doc.items():
                doc_to_write += (str(value) + ',')
            doc_to_write += ('\n')
        return doc_to_write

    # NEW
    def prep_listofdict_csv(self, json_doc):
        """Prepares a JSON document containing a list of dictionaries for writing to a CSV file.
        Parameters:
        json_doc -> a raw json document containing a list of dictionaries
        """
        doc_to_write = ''
        header = []
        for key in json_doc[0].keys():
            header.append(key)
        doc_to_write += (','.join(header)+'\n')
        for entry in json_doc:
            for value in entry.values():
                doc_to_write += (str(value) + ',')
            doc_to_write += ('\n')
        return doc_to_write

    # NEW
    def prep_singledict_csv(self, json_dict, orientation='horizontal', in_list=False):
        """Prepares a JSON document containing a single dictionary for writing to a CSV file.
        Parameters:
        json_doc -> a raw json document containing a single dictionary
        orientation -> the layout of the data. Accepted arguments:
        - 'horizontal' in which the keys are in the first row
        - 'vertical' in which the keys are in the first column
        in_list -> in some situations, the single dictionary is nested inside a list, True will return the 0 index of that list. Default False.
        """
        doc_to_write = ''
        if in_list:
            dictionary = json_dict[0].items()
        else:
            dictionary = json_dict.items()
        if orientation == 'horizontal':
            header = []
            values = []
            for key, value in dictionary:
                header.append(key)
                values.append(value)
            doc_to_write += (','.join(header))
            doc_to_write += (','.join(map(str, values)))
        elif orientation == 'vertical':
            for key, value in json_dict.items():
                doc_to_write += (str(key) + ',' + str(value) + '\n')
        return doc_to_write

    def write_block_to_csv(self, doc_to_write, filename_addition):
        """Writes a block or list of preformated string(s) to a csv file.
        Parameters:
        doc_to_write -> the preformatted string or list to write
        filename_addition -> the identifier that will be tacked onto the filename.
        """
        if isinstance(doc_to_write, list):
            block_to_write = ''
            for string in list_to_write:
                block_to_write += string
            with open(self.csvfile_base.replace('%s', filename_addition), 'w+') as f:
                f.write(block_to_write)
        else:
            with open(self.csvfile_base.replace('%s', filename_addition), 'w+') as f:
                f.write(doc_to_write)


    #  ___          _                   _   ___     _          ___       __                    _   _
    # | _ ) __ _ __(_)__   __ _ _ _  __| | | _ \_ _(_)__ ___  |_ _|_ _  / _|___ _ _ _ __  __ _| |_(_)___ _ _
    # | _ \/ _` (_-< / _| / _` | ' \/ _` | |  _/ '_| / _/ -_)  | || ' \|  _/ _ \ '_| '  \/ _` |  _| / _ \ ' \
    # |___/\__,_/__/_\__| \__,_|_||_\__,_| |_| |_| |_\__\___| |___|_||_|_| \___/_| |_|_|_\__,_|\__|_\___/_||_|


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

    def get_historical_price(self, time_frame, date=None, chart_by_day=False, chart_close_only=False, csv=None):
        """10 credits per day requested when part of a time frame. (Full Data)
        50 credits per single day, minute data.
        Parameters:
        time_frame -> String. Determines how far back to retrieve data. Set to 'date' if only one specific day is required.
        date -> String. If 'date' is specified in time_frame, this is the date that you wish to access.
        chart_by_date -> Boolean. If a single date is requested, setting param to True only returns OHLC data instead of minutely data.
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.

        """
        result = stock.new_historical_price(self.ticker, period=time_frame, date=date, chart_by_day=chart_by_day, chart_close_only=chart_close_only)
        attribute_name = f"{period}_historical_price"
        setattr(IEXStock, attribute_name, result)
        if csv == 'prep':
            return self.prep_price_json_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_price_json_csv(result), 'time_frame')
            return result
        else:
            return result

    #  ___ _                   _      _   ___ _        _                     _
    # | __(_)_ _  __ _ _ _  __(_)__ _| | / __| |_ __ _| |_ ___ _ __  ___ _ _| |_ ___
    # | _|| | ' \/ _` | ' \/ _| / _` | | \__ \  _/ _` |  _/ -_) '  \/ -_) ' \  _(_-<
    # |_| |_|_||_\__,_|_||_\__|_\__,_|_| |___/\__\__,_|\__\___|_|_|_\___|_||_\__/__/


    def get_balance_sheet(self, period=None, last=None, csv=None):
        # HORIZONTAL
        """3,000 credits per symbol requested.
        Returns balance sheet data for the requested company.
        Sets class attribute 'self.balance_sheet'.
        Parameters:
        period -> String. Accepts ['annual', 'quarterly']. Defaults to quarterly
        last -> Integer. Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.balance_sheet(self.ticker, period=period, last=last)
        self.balance_sheet = result
        if csv == 'prep':
            self.balance_sheet = self.prep_financial_json_csv(result, 'balancesheet')
        if csv == 'output':
            self.write_block_to_csv(self.prep_financial_json_csv(result, 'balancesheet'), 'balancesheet')
        return result

    def get_income_statement(self, period=None, last=None, csv=None):
        # HORIZONTAL
        """1,000 credits per symbol requested.
        Returns income statement data for the requested company and sets class attribute 'self.income_statement'.
        Parameters:
        period -> String. Accepts ['annual', 'quarterly']. Defaults to quarterly
        last -> Integer. Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.income_statement(self.ticker, period=period, last=last)
        self.income_statement = result
        if csv == 'prep':
            self.income_statement =  self.prep_financial_json_csv(result, 'income')
        if csv == 'output':
            self.write_block_to_csv(self.prep_financial_json_csv(result, 'income'), 'incomestatement')
        return result

    def get_cash_flow_statement(self, period=None, last=None, csv=None):
        # HORIZONTAL
        """1,000 credits per symbol requested.
        Returns cash flow statement data for the requested company and sets class attribute 'self.cash_flow_statement'.
        Parameters:
        period -> String. Accepts ['annual', 'quarterly'], defaults to quarterly
        last -> Integer. Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.cash_flow(self.ticker, period=period, last=last)
        self.cash_flow_statement = result
        if csv == 'prep':
            self.cash_flow_statement = self.prep_financial_json_csv(result, 'cashflow')
        if csv == 'output':
            self.write_block_to_csv(self.prep_financial_json_csv(result, 'cashflow'), 'cashflow')
        return result

    #  ___ _____  __  __  __     _   _            _
    # |_ _| __\ \/ / |  \/  |___| |_| |_  ___  __| |___
    #  | || _| >  <  | |\/| / -_)  _| ' \/ _ \/ _` (_-<
    # |___|___/_/\_\ |_|  |_\___|\__|_||_\___/\__,_/__/


    def get_advanced_fundementals(self, period, csv=None):
        # Vertical
        """75,000 credits per symbol requested.
        Returns immediate access to the data points in IEX models for 2850+ companies. Models are updated daily.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'advanced_fundementals'.
        Parameters:
        period -> string, accepted values ['annual', 'quarterly', 'ttm']
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.advanced_fundementals(self.ticker, period)
        self.advanced_fundementals = result
        if csv == 'prep':
            self.advanced_fundementals = self.prep_singledict_csv(result, orientation='vertical', in_list=True)
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_csv(result, orientation='vertical', in_list=True), 'advanced_fundementals')
        return result

    def get_advanced_stats(self, csv=None):
        # Vertical
        """3,005 credits per symbol requested.
        Returns a buffed version of key stats with selected financial data and more. Includes all data points from 'key stats'.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'advanced_stats'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.advanced_stats(self.ticker)
        self.advanced_stats = result
        if csv == 'prep':
            self.advanced_stats = self.prep_singledict_csv(result, orientation='vertical')
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_csv(result, orientation='vertical'), 'advanced_stats')
        return result

    #  ___         _            _ #
    # | _ )_ _ ___| |_____ _ _ | |#
    # | _ \ '_/ _ \ / / -_) ' \|_|#
    # |___/_| \___/_\_\___|_||_(_)#

#    def get_book(self, csv=None):
#        # Vertical
#        """1 credit per symbol requested.
#        Returns quote, bid, ask, etc. data for the requested symbol.
#        Real time data available.
#        CSV is formatted vertically with keys in the first column.
#        Sets class attribute 'book'.
#        Parameters:
#        csv -> string. Determines the processing for csv files. Valid arguments are:
#        - 'output' will create a new CSV file with just the data from this endpoint.
#        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
#        """
#        result = stock.book(self.ticker)
#        self.book = result
#        if output_csv:
#            self.convert_singledict_csv(result, 'book', orientation='vertical')
#        return result

    def get_company(self, csv=None):
        # Vertical
        """1 credit per symbol requested.
        Returns general information on the company requested.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'company'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.company(self.ticker)
        self.company = result
        if csv == 'prep':
            self.company = self.prep_singledict_csv(result, orientation='vertical')
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_csv(result, orientation='vertical'), 'company')
        return result

    def get_delayed_quote(self, csv=None):
        # Vertical
        """1 credit per symbol requested.
        Returns 15 minute delayed quote for the requested symbol.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'delayed_quote'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.

        """
        result = stock.delayed_quote(self.ticker)
        self.delayed_quote = result
        if csv == 'prep':
            self.delayed_quote = self.prep_singledict_csv(result, orientation='vertical')
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_csv(result, orientation='vertical'), 'delayed_quote')
        return result

    def get_dividends(self, scope, csv=None):
        # Vertical
        """10 credits per symbol requested.
        Returns basic dividend information for the requested symbol.
        Sets class attribute 'dividends'.
        Parameters:
        scope -> string, the range of data needed. Accepted arguments: ['5y','2y','1y','ytd','6m','3m','1m','next']
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.

        """
        result = stock.dividends(self.ticker, scope)
        self.dividends = result
        if csv == 'prep':
            self.dividends = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'dividends')
        return result

    def get_basic_financials(self, csv=None):
        # Horizontal
        """5000 credits per symbol requested.
        Returns basic financial data from the requested company.
        Note that fetching all three full financial statements has the same credit cost as this endpoint.
        Sets class attribute 'basic_financials'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.financials(self.ticker)
        self.basic_financials = result
        if csv == 'prep':
            self.basic_financials = self.prep_financial_json_csv(result, 'financials')
        if csv == 'output':
            self.write_block_to_csv(self.prep_financial_json_csv(result, 'financials'), 'basic_financials')
        return result

    def get_fund_ownership(self, csv=None):
        # Horizontal - Needs to be Changed
        """10,000 credits per symbol requested.
        Returns the 10 largest institutional holders of the requested company.
        Sets class attribute 'fund_ownership'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.fund_ownership(self.ticker)
        self.fund_ownership = result
        if csv == 'prep':
            self.fund_ownership = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'fund_ownership')
        return result

    def get_insider_roster(self, output_csv):
        # Horizontal
        """5,000 credits per symbol requested.
        Returns the top 10 insiders, with the most recent information.
        Sets class attribute 'insider_roster'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.

        """
        result = stock.insider_roster(self.ticker)
        self.insider_roster = result
        if csv == 'prep':
            self.insider_roster = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'insider_roster')
        return result

    def get_insider_transactions(self, output_csv):
        # Horizontal
        """50 credits per transaction per symbol requested.
        Returns insider transactions with the most recent information.
        Sets class attribute 'insider_transactions'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.insider_transactions(self.ticker)
        self.insider_transactions = result
        if csv == 'prep':
            self.insider_transactions = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'insider_transactions')
        return result

    def get_institutional_ownership(self, csv=None):
        # Horizontal
        """10,000 credits per symbol requested
        Returns the 10 largest instituional owners for the requested stock. This is defined as explicitly buy or sell-side only.
        Sets class attribute 'institutional_ownership'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.institutional_ownership(self.ticker)
        self.institutional_ownership = result
        if csv == 'prep':
            self.institutional_ownership = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'institutional_ownership')
        return result

    def get_key_stats(self, stat=None, csv=None):
        # Vertical
        """5 credits per symbol requested, 1 credit per stat per symbol requested.
        Returns important stats for the requested company.
        Sets class attribute 'key_stats'.
        CSV is formatted vertically with keys in the first column.
        Parameters:
        stat -> String. If you would like to querie one single stat, you can enter that here.
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.key_stats(self.ticker, stat=stat)
        self.key_stats = result
        if csv == 'prep':
            self.key_stats = self.prep_singledict_csv(result, orientation='vertical')
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_csv(result, orientation='vertical'), 'key_stats')
        return result

    def get_largest_trades(self, csv=None):
        # Horizontal
        """1 credit per trade per symbol requested.
        This returns 15 minute delayed, last sale eligible trades.
        Sets class attribute 'largest_trades'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.largest_trades(self.ticker)
        self.largest_trades = result
        if csv == 'prep':
            self.largest_trades = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'largest_trades')
        return result

    def get_logo(self):
        """1 credit per symbol requested
        Returns a Google APIs link (bare url string) to the logo for the requested stock.
        Sets class attribute 'logo'.
        """
        result = stock.logo(self.ticker)['url']
        self.logo = result
        return result

    def get_news(self,last=10, csv=None):
        # Horizontal
        """1 credit per news article per symbol requested.
        Provides intraday news from over 3,000 global news sources including major publications, regional media, and social.
        Sets class attribute 'news'.
        Parameters ->
        last -> Integer. Number of article to return. Min = 1 Max = 50 Defualt = 10
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.news(self.ticker, last=last)
        self.news = result
        if csv == 'prep':
            self.news = self.prep_listofdict_csv(result)
        if csv == 'output':
            self.write_block_to_csv(self.prep_listofdict_csv(result), 'news')
        return result

    def get_ohlc(self, csv=None):
        # Horizontal
        """2 credits per symbol requested.
        Returns the official open and close for a give symbol.
        Sets class attribute 'ohlc'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.ohlc(self.ticker)
        self.ohlc = result
        if csv == 'prep' or 'output':
            prepped_data = ''
            prepped_data += (result[0])
            for key, value in result[0].items():
                prepped_data += (key + ',' + str(value) + '\n')
            prepped_data += (result[1])
            for key, value in result[1].items():
                prepped_data += (key + ',' + str(value) + '\n')
            for key,value in result[2:].items():
                prepped_data += (key + ',' + str(value) + '\n')
            if csv == 'prep':
                self.ohlc = prepped_data
            if output == 'output':
                write_block_to_csv(prepped_data, 'ohlc')
        return result

    def get_peers(self):
        """500 credits per symbol requested.
        Returns a list of peer company's tickers in Python list form.
        Sets class attribute 'peers'.
        """
        result = stock.peers(self.ticker)
        self.peers = result
        return result

    def get_quote(self, csv=None):
        # Vertical
        """1 credit per symbol requested.
        Returns quote data for the requested symbol.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'quote'.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        - 'output' will create a new CSV file with just the data from this endpoint.
        - 'prep' will set the corrosponding class attribute to the formatted string instead of the raw json.
        """
        result = stock.quote(self.ticker)
        self.quote = result
        if csv == 'prep':
            self.quote = self.prep_singledict_csv(result, orientation='vertical')
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_csv(result, orientation='vertical'), 'quote')
        return result

class IEXMarket():
    def __init__(self):
        self.date = date.today()
        self.available_economic_symbols = {
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
        self.available_commodity_symbols = {
        'DCOILWTICO':'Crude oil West Texas Intermediate - in dollars per barrel, not seasonally adjusted',
        'DCOILBRENTEU':'Crude oil Brent Europe - in dollars per barrel, not seasonally adjusted',
        'DHHNGSP':'Henry Hub Natural Gas Spot Price - in dollars per million BTU, not seasonally adjusted',
        'DHOILNYH':'No. 2 Heating Oil New York Harbor - in dollars per gallon, not seasonally adjusted',
        'DJFUELUSGULF':'Kerosense Type Jet Fuel US Gulf Coast - in dollars per gallon, not seasonally adjusted',
        'GASDESW':'US Diesel Sales Price - in dollars per gallon, not seasonally adjusted',
        'GASREGCOVW':'US Regular Conventional Gas Price - in dollars per gallon, not seasonally adjusted',
        'GASMIDCOVW':'US Midgrade Conventional Gas Price - in dollars per gallon, not seasonally adjusted',
        'GASPRMCOVW':'US Premium Conventional Gas Price - in dollars per gallon, not seasonally adjusted',
        'DPROPANEMBTX':'Propane Prices Mont Belvieu Texas - in dollars per gallon, not seasonally adjusted'
        }

    def get_market_datapoint(self, symbol, key='market', **queries):
        """1,000 credits per symbol requested per date.
        Returns various economic and commodity values as a datapoint.
        Sets a class attribute equal to the symbol requested.
        Parameters:
        symbol -> The symbol of the economic indicator or commodity datapoint requested.
        Class attribute 'available_economic_symbols' is a dictionary of available economic symbols and their description.
        Class attribute 'available_commodity_symbols' is a dictionary of available commodity symbols and their description
        """
        result = market.generic_data_point(symbol, key, **queries)
        setattr(IEXMarket, symbol, result)
        return result

    def get_all_economic_data(self, output_csv=False):
        """18,000 credits per request per day.
        Returns all available current economic indicator datapoints.
        Parameters:
        csv -> string. Determines the processing for csv files. Valid arguments are:
        """
        output_data = {}
        for key in self.available_commodity_symbols.keys():
            output_data[key] = market.generic_data_point(key, 'market')
        if output_csv:
            with open(f'{self.date}_economic_data.csv', 'w+') as f:
                for key, value in output_data.items():
                    f.write(str(key) + ',' + str(value) + '\n')
        return output_data

    def get_all_commodity_data(self, output_csv=False):
        """10,000 credits per request per day.
        Returns all available current commodity datapoints.
        """
        output_data = {}
        for key in self.available_commodity_symbols.keys():
            output_data[key] = market.generic_data_point(key, 'market')
        if output_csv:
            with open(f'{self.date}_commodity_data.csv', 'w+') as f:
                for key, value in output_data.items():
                    f.write(str(key) + ',' + str(value) + '\n')
        return output_data
