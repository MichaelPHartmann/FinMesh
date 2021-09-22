from datetime import date
import types
import pickle
import pandas

from .stock import *
from .premium import *
from .market import *
from ._common import *


class IEXStock:
    """A class that is built around retrieving data from the IEX Cloud API service.
    All available data is derived from functions defined in the stock.py module, and are implemented here with a "get_" prefix.
    All data is available in CSV format, and can be grouped together for bulk file writing.
    CSV data is parsed, built and written using a scratch-built parser and this is why there is not currently any Excel output options.
    Beta version will use Pandas. This is currently about 75% completed.
    All data retrieved is automatically stored in the corrosponding class attribute (sans "get_" prefix).
    Data set to class attributes can be saved to file and subsequently loaded from that file to limit credit usage in IEX Cloud.

    :param ticker: The symbol or ticker of the stock for which the class is to be created.
    :type ticker: string, required
    :param period: Default is 'quarter'. Allows a user to set period data for all income statement requests.
    :type period: string, optional
    :param last: Default is 1. Allows a user to specify how many statements to retrieve of financial statement data.
    :type last: integer, optional
    :param autopopulate: Automatically populates key information as class attributes. Uses methods 'basic_information' and 'price_information'
    :type autopopulate: boolean, optional
    """
    def __init__(self, ticker, period='quarter', last=1, autopopulate=False):
        self.ticker = ticker
        self.period = period
        self.last = last
        self.csvfile_base = f'{ticker}_%s.csv' # TO BE DEPRECATED #
        self.excelfile_base = f'{ticker}_%s.xlsx' # TO BE DEPRECATED #
        self.genfile_base = f'{ticker}_%s'
        self.set_date()

        if autopopulate:
            self.basic_information()
            self.price_information()
            if self.build_savestate_file(addin='pickle') in os.listdir():
                self.load_state(input='pickle')
            if self.build_savestate_file() in os.listdir():
                self.load_state(input='plaintext')

    def set_date(self):
        """Sets the date attribute.
        This is needed keep save and load funcionality smooth.
        """
        result = str(date.today())
        setattr(IEXStock, 'date', result)

    def filename_builder(extension, filename_addition):
        return self.genfile_base.replace('%s', filename_addition).append(extension)

    def pickle_class_state(self):
        """This method takes the current state of the class and pickles it as-is.
        This will preserve all attributes of the current class instance.
        Recalling/loading the class can be done with the ``iex.unpickle_class_state()``
        Filename is automatically created as '#ticker#_#date#_pickle.pickle'
        """
        filename = filename_builder('.pickle', f'{self.date}')
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    # TO BE DEPRECATED #
    def build_savestate_file(self, addin=None):
        """:meta private:
        Builds a standard file name based on an add-in.
        This allows automatic retrieval of savestate files because the files are created using the exact same method.
        Parameters:
        addin -> String. File identifier to aid in automated loading of savestate files.
        """
        result = f'{self.ticker}_{self.date}_savestate'
        if addin:
            result = result + f'_{addin}.txt'
        else:
            result = result + '.txt'

    # TO BE DEPRECATED #
    def save_state(self, output='plaintext', directory=None):
        """:meta private:
        Saves the current initialized state attributes in a serialized text file.
        Currently only outputs dicts into a .txt file.
        Parameters:
        output -> String. Defines the type of output. Default is plaintext.
        directoy -> String. If the saved file is to be put in a directory, this is the name of that directory.
        """
        # Build a list of attributes for the class
        result = []
        for attr in dir(self):
            if not attr.startswith('__'):
                if not isinstance(self.__getattribute__(attr), types.MethodType):
                    result.append(attr)
        # Prepare the data to be written
        raw_to_write = ''
        raw_to_write += ('[\n')
        for r in result:
            attr_to_save = {r:self.__getattribute__(r)}
            raw_to_write += (str(attr_to_save)+',\n')
        raw_to_write += (']')
        # Standard filepath builder
        if output == 'pickle': filepath = self.build_savestate_file(addin='pickle')
        else: filepath = self.build_savestate_file()
        if directory:
            dir_strip = directory.strip('/')
            filepath = f'{dir_strip}/' + filepath

        if output == 'pickle':
            pickle_to_write = pickle.dumps(raw_to_write)
            with open(filepath, 'w+') as f:
                f.write(pickle_to_write)
        else:
            with open(filepath, 'w+') as f:
                f.write(raw_to_write)

    # TO BE DEPRECATED #
    def load_state(self, input='plaintext', directory=None):
        """:meta private:
        Loads the attributes of a previous serialized class and it's attributes from a file.
        Parameters:
        input -> String. Defines the type of input. Default is plaintext.
        directoy -> String. If the saved file is in a directory, this is the name of that directory.
        """
        # Standard filepath builder
        if input == 'pickle': filepath = self.build_savestate_file(addin='pickle')
        else: filepath = self.build_savestate_file()
        if directory:
            dir_strip = directory.strip('/')
            filepath = f'{dir_strip}/' + filepath

        if input == 'pickle':
            literal_list = pickle.load(filepath)
        else:
            with open(filepath, 'r') as file:
                save_data = file.read()
                literal_list = eval(save_data)

        for dict in literal_list:
            for key, value in dict.items():
                setattr(IEXStock, key, value)

    #  _  _     _                 ___             _   _
    # | || |___| |_ __  ___ _ _  | __|  _ _ _  __| |_(_)___ _ _  ___
    # | __ / -_) | '_ \/ -_) '_| | _| || | ' \/ _|  _| / _ \ ' \(_-<
    # |_||_\___|_| .__/\___|_|   |_| \_,_|_||_\__|\__|_\___/_||_/__/
    #            |_|


    def pandas_financial_json(self, json, statement):
        """Returns a dataframe for the requested financial statement.

        :param json: the raw json output from IEX Cloud containing financial statement data.
        :type json: string, raw json, required
        :param statement: the name of the statement as used by IEX Cloud.
        :type statement: accepted values are : 'balancesheet', 'incomestatement', and 'cashflow'.
        """
        data_to_frame = {}
        header = []
        for key in json[statement][0].keys():
            header.append(key)
        for key in header:
            list_of_values = []
            for year in range(len(json[statement])-1):
                list_of_values.append(json[statement][year][key])
            data_to_frame[key] = list_of_values
        dataframe = pandas.DataFrame(data_to_frame)
        return dataframe

    # TO BE DEPRECATED #
    def prep_financial_json(self, json, statement):
        """:meta private:
        Prepares a JSON document containing a financial data for writing to a CSV file.
        Parameters:
        json -> a raw json document containing financial data
        statement -> the name of the statement as used by IEX Cloud. Accepted values are : 'balancesheet', 'incomestatement', and 'cashflow'.
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


    def pandas_price_json(self, json):
        """Returns a dataframe for the requested price statement.

        :param json: the raw json output from IEX Cloud containing daily price data.
        :type json: raw json
        """
        data_to_frame = {}
        header = []
        for key in json_doc[0].keys():
            header.append(key)
        for key in header:
            list_of_values = []
            for day in range(len(json)-1):
                list_of_values.append(json[day][key])
            data_to_frame[key] = list_of_values
        dataframe = pandas.DataFrame(data_to_frame)
        return dataframe

    # TO BE DEPRECATED #
    def prep_price_json(self, json_doc):
        """:meta private:
        Prepares a JSON document containing a stock price data for writing to a CSV file.

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


    def pandas_listofdict_json(self, json):
        """Returns a dataframe for the requested list of dictionaries json document.

        :param json: the raw json output from IEX Cloud containing a list of dictionary.
        :type json: raw json
        """
        data_to_frame = {}
        header = []
        for key in json_doc[0].keys():
            header.append(key)
        for key in header:
            list_of_values = []
            for entry in json:
                list_of_values.append(entry[key])
            data_to_frame[key] = list_of_values
        dataframe = pandas.DataFrame(data_to_frame)
        return dataframe

    # TO BE DEPRECATED #
    def prep_listofdict_json(self, json_doc):
        """:meta private:
        Prepares a JSON document containing a list of dictionaries for writing to a CSV file.
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

    def pandas_singledict_json(self, json, in_list=False):
        """Returns a dataframe for the requested dictionary json document.

        :param json: the raw json output from IEX Cloud containing a list of dictionary.
        :type json: raw json
        :param in_list: whether the disctionary is conatined within a list element, that is, inside square braces.
        :type in_list: boolean
        """
        data_to_frame = {}
        if in_list:
            dictionary = json[0]
        else:
            dictionary = json
        for key, value in dictionary.items():
            data_to_frame[key] = value
        dataframe = pandas.DataFrame(data_to_frame, index=[0])
        return dataframe

    # TO BE DEPRECATED #
    def prep_singledict_json(self, json_dict, orientation='horizontal', in_list=False):
        """:meta private:
        Prepares a JSON document containing a single dictionary for writing to a CSV file.
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

    # TO BE DEPRECATED #
    def write_block_to_csv(self, doc_to_write, filename_addition):
        """:meta private:
        Writes a block or list of preformated string(s) to a csv file.
        Functionally identical to 'custom_write_block_to_csv' method but uses a standardized method to build the filename.
        Mainly used as optional output in class and csv savestate methods.
        Parameters:
        doc_to_write -> the preformatted string or list of preformated strings to write.
        filename_addition -> the identifier that will be tacked onto the filename.
        """
        if isinstance(doc_to_write, list):
            block_to_write = ''
            for string in doc_to_write:
                block_to_write += string
            with open(self.csvfile_base.replace('%s', filename_addition), 'w+') as f:
                f.write(block_to_write)
        else:
            with open(self.csvfile_base.replace('%s', filename_addition), 'w+') as f:
                f.write(doc_to_write)

    # TO BE DEPRECATED #
    def custom_write_block_to_csv(self, doc_to_write, filename):
        """:meta private:
        Writes a block or list of preformated string(s) to a csv file.
        Functionally identical to 'write_block_to_csv' method but does not use a standardized filename builder to determine the file name.
        Parameters:
        doc_to_write -> the preformatted string or list of preformated strings to write.
        filename -> the filename to write to. If the file exists it will be over written. Include '.csv' appendation.
        """
        if isinstance(doc_to_write, list):
            block_to_write = ''
            for string in doc_to_write:
                block_to_write += string
            with open(filename, 'w+') as f:
                f.write(block_to_write)
        else:
            with open(filename, 'w+') as f:
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

        :return: Most recent price for the requested company and sets class attribute 'self.price'.
        """
        result = stock.price(self.ticker)
        self.price = result
        return result

    def get_historical_price(self, time_frame, date=None, chart_by_day=False, chart_close_only=False, output=None):
        """10 credits per day requested when part of a time frame. (Full Data)
        50 credits per single day, minute data.

        :param time_frame: Determines how far back to retrieve data. Set to 'date' if only one specific day is required.
        :type time_frame: string
        :param date: If 'date' is specified in time_frame, this is the date that you wish to access.
        :type date: string
        :param chart_by_date: If a single date is requested, setting param to True only returns OHLC data instead of minutely data.
        :type chart_by_date: boolean
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.new_historical_price(self.ticker, period=time_frame, date=date, chart_by_day=chart_by_day, chart_close_only=chart_close_only)
        attribute_name = f"{period}_historical_price"

        if output:
            result = pandas_price_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv', period))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', period))

        setattr(IEXStock, attribute_name, result)
        return result

    #  ___ _                   _      _   ___ _        _                     _
    # | __(_)_ _  __ _ _ _  __(_)__ _| | / __| |_ __ _| |_ ___ _ __  ___ _ _| |_ ___
    # | _|| | ' \/ _` | ' \/ _| / _` | | \__ \  _/ _` |  _/ -_) '  \/ -_) ' \  _(_-<
    # |_| |_|_||_\__,_|_||_\__|_\__,_|_| |___/\__\__,_|\__\___|_|_|_\___|_||_\__/__/


    def get_balance_sheet(self, period=None, last=None, output=None):
        """3,000 credits per symbol requested.

        Sets class attribute 'self.balance_sheet'

        :return: Balance sheet data for the requested company. If any non-JSON output is chosen, the method will return a Pandas DataFrame with the data from this endpoint.

        :param period: Time interval of statements. Defaults to quarterly
        :type period: accepted values are ['annual', 'quarterly'], optional
        :param last: Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        :type last: integer, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.balance_sheet(self.ticker, period=period, last=last)

        if output:
            result = self.pandas_financial_json(result, 'balancesheet')
            if output == 'csv':
                result.to_csv(filename_builder('.csv','balancesheet'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'balancesheet'))

        self.balance_sheet = result
        return result

    def get_income_statement(self, period=None, last=None, output=None):
        # HORIZONTAL
        """1,000 credits per symbol requested.

        Sets class attribute 'self.income_sheet'

        :return: Income sheet data for the requested company. If any non-JSON output is chosen, the method will return a Pandas DataFrame with the data from this endpoint.

        :param period: Time interval of statements. Defaults to quarterly
        :type period: accepted values are ['annual', 'quarterly'], optional
        :param last: Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        :type last: integer, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.income_statement(self.ticker, period=period, last=last)

        if output:
            result = self.pandas_financial_json(result, 'income')
            if output == 'csv':
                result.to_csv(filename_builder('.csv','income'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'income'))

        self.income_statement = result
        return result

    def get_cash_flow_statement(self, period=None, last=None, output=None):
        # HORIZONTAL
        """1,000 credits per symbol requested.

        Sets class attribute 'self.cash_flow_statement'

        :return: Cash flow statement data for the requested company. If any non-JSON output is chosen, the method will return a Pandas DataFrame with the data from this endpoint.

        :param period: Time interval of statements. Defaults to quarterly
        :type period: accepted values are ['annual', 'quarterly'], optional
        :param last: Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        :type last: integer, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        if period is None:
            period = self.period
        if last is None:
            last = self.last
        result = stock.cash_flow(self.ticker, period=period, last=last)

        if output:
            result = self.pandas_financial_json(result, 'income')
            if output == 'csv':
                result.to_csv(filename_builder('.csv','income'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'income'))

        self.cash_flow_statement = result
        return result

    def get_financial_statements(self, period=None, last=None, output=None):
        """5,000 credits per symbol requested.
        This is useful if you want to update the query parameters after you've made some requests. It's just a time saver.

        :return: All financial statement data for the requested company and sets class attribute for each individual statement, and returns a list of the attribute names.

        :param period: Time interval of statements. Defaults to quarterly
        :type period: accepted values are ['annual', 'quarterly'], optional
        :param last: Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        :type last: integer, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        self.get_balance_sheet(period=period, last=last, csv=csv)
        self.get_cash_flow_statement(period=period, last=last, csv=csv)
        self.get_income_statement(period=period, last=last, csv=csv)
        return [self.balance_sheet, self.cash_flow_statement, self.income_statement]

    #  ___ _____  __  __  __     _   _            _
    # |_ _| __\ \/ / |  \/  |___| |_| |_  ___  __| |___
    #  | || _| >  <  | |\/| / -_)  _| ' \/ _ \/ _` (_-<
    # |___|___/_/\_\ |_|  |_\___|\__|_||_\___/\__,_/__/


    def get_advanced_fundementals(self, period, output=None):
        # Vertical
        """75,000 credits per symbol requested.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'advanced_fundementals'

        :return: Immediate access to the data points in IEX models for 2850+ companies. Models are updated daily.

        :param period: Time interval of statements. Defaults to quarterly
        :type period: accepted values are ['annual', 'quarterly'], optional
        :param last: Number of periods to return, up to 4 for annual and 16 for quarterly. Defaults to 1.
        :type last: integer, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.advanced_fundementals(self.ticker, period)

        if output:
            result = self.pandas_singledict_json(result, in_list=False)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','advanced_fundementals'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'advanced_fundementals'))

        self.advanced_fundementals = result
        return result

    def get_advanced_stats(self, output=None):
        # Vertical
        """3,005 credits per symbol requested.
        Sets class attribute 'advanced_stats'.

        :return: Buffed version of key stats with selected financial data and more. Includes all data points from 'key stats'.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.advanced_stats(self.ticker)

        if output:
            result = self.pandas_singledict_json(result, in_list=False)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','advanced_stats'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'advanced_stats'))

        self.advanced_stats = result
        return result

    #  ___         _            _ #
    # | _ )_ _ ___| |_____ _ _ | |#
    # | _ \ '_/ _ \ / / -_) ' \|_|#
    # |___/_| \___/_\_\___|_||_(_)#

#    def get_book(self, output=None):
#        # Vertical
#        """1 credit per symbol requested.
#        Returns quote, bid, ask, etc. data for the requested symbol.
#        Real time data available.
#        CSV is formatted vertically with keys in the first column.
#        Sets class attribute 'book'.
#        Parameters:
#        output -> string. Determines the output of the data. Default is raw JSON.
#        If any non-JSON output is chosen, the method will return a Pandas DataFrame with the data from this endpoint.
#        Valid arguments are:
#        - 'dataframe' will create a pandas data frame with the data from this endpoint.
#        - 'csv' will create a CSV file with the data from this endpoint. Uses Pandas.
#        """
#        result = stock.book(self.ticker)
#        self.book = result
#        if output_csv:
#            self.convert_singledict_csv(result, 'book', orientation='vertical')
#        return result

    def get_company(self, output=None):
        # Vertical
        """1 credit per symbol requested.
        Sets class attribute 'company'.

        :return: General information on the company requested.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.company(self.ticker)

        if output:
            result = self.pandas_singledict_json(result, in_list=False)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','company'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'company'))

        self.company = result
        return result

    def get_delayed_quote(self, output=None):
        # Vertical
        """1 credit per symbol requested.
        Sets class attribute 'delayed_quote'.

        :return: 15 minute delayed quote for the requested symbol.


        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.delayed_quote(self.ticker)

        if output:
            result = self.pandas_singledict_json(result, in_list=False)
            if output == 'csv':
                result.to_csv(filename_builder('.csv', 'delayed_quote'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'delayed_quote'))

        self.delayed_quote = result
        return result

    def get_dividends(self, scope, output=None):
        # Vertical
        """10 credits per symbol requested.
        Sets class attribute 'dividends'.

        :return: Basic dividend information for the requested symbol.


        :param scope: the range of data needed.
        :type scope: accepted arguments: ['5y','2y','1y','ytd','6m','3m','1m','next'], required
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.dividends(self.ticker, scope)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','dividends'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','dividends'))

        self.dividends = result
        return result

    def get_basic_financials(self, output=None):
        # Horizontal
        """5000 credits per symbol requested.
        Note that fetching all three full financial statements has the same credit cost as this endpoint.
        Sets class attribute 'basic_financials'.

        :return: Basic financial data from the requested company.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.financials(self.ticker)
        self.basic_financials = result
        if csv == 'prep':
            self.basic_financials = self.prep_financial_json(result, 'financials')
        if csv == 'output':
            self.write_block_to_csv(self.prep_financial_json(result, 'financials'), 'basic_financials')
        return result

    def get_fund_ownership(self, output=None):
        # Horizontal - Needs to be Changed
        """10,000 credits per symbol requested.
        Sets class attribute 'fund_ownership'.

        :return: 10 largest institutional holders of the requested company.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.fund_ownership(self.ticker)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','fund_ownership'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','fund_ownership'))

        self.fund_ownership = result
        return result

    def get_insider_roster(self, output=None):
        # Horizontal
        """5,000 credits per symbol requested.
        Sets class attribute 'insider_roster'.

        :return: Top 10 insiders, with the most recent information.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.insider_roster(self.ticker)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','insider_roster'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','insider_roster'))

        self.insider_roster = result
        return result

    def get_insider_transactions(self, output=None):
        # Horizontal
        """50 credits per transaction per symbol requested.
        Sets class attribute 'insider_transactions'.

        :return: Insider transactions with the most recent information.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.insider_transactions(self.ticker)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','insider_transactions'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','insider_transactions'))

        self.insider_transactions = result
        return result

    def get_institutional_ownership(self, output=None):
        # Horizontal
        """10,000 credits per symbol requested.
        Sets class attribute 'institutional_ownership'.

        :return: 10 largest instituional owners for the requested stock. This is defined as explicitly buy or sell-side only.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.institutional_ownership(self.ticker)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','institutional_ownership'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','institutional_ownership'))

        self.institutional_ownership = result
        return result

    def get_key_stats(self, stat=None, output=None):
        # Vertical
        """5 credits per symbol requested, 1 credit per stat per symbol requested.
        Sets class attribute 'key_stats'.

        :return: Important stats for the requested company.

        :param stat: If you would like to querie one single stat, you can enter that here.
        :type stat: string, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.key_stats(self.ticker, stat=stat)

        if output:
            result = self.pandas_singledict_json(result, in_list=False)
            if output == 'csv':
                result.to_csv(filename_builder('.csv', 'key_stats'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'key_stats'))

        self.key_stats = result
        return result

    def get_largest_trades(self, output=None):
        # Horizontal
        """1 credit per trade per symbol requested.
        Sets class attribute 'largest_trades'.

        :return: 15 minute delayed, last sale eligible trades.

        :param stat: If you would like to querie one single stat, you can enter that here.
        :type stat: string, optional
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.largest_trades(self.ticker)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','largest_trades'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','largest_trades'))

        self.largest_trades = result
        return result

    def get_logo(self):
        """1 credit per symbol requested.
        Sets class attribute 'logo'.

        :return: Google APIs link (bare url string) to the logo for the requested stock.
        """
        result = stock.logo(self.ticker)['url']
        self.logo = result
        return result

    def get_news(self,last=10, output=None):
        # Horizontal
        """1 credit per news article per symbol requested.
        Sets class attribute 'news'.

        :return: Intraday news from over 3,000 global news sources including major publications, regional media, and social.

        :param last: Number of article to return. Defualt = 10
        :type last: integer, min = 1 max = 50
        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.news(self.ticker, last=last)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','news'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','news'))

        self.news = result
        return result

    def get_ohlc(self, output=None):
        # Horizontal
        """2 credits per symbol requested.
        Sets class attribute 'ohlc'.

        :return: Official open and close for a give symbol.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
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
        Sets class attribute 'peers'.

        :return: List of peer company's tickers in Python list form.
        """
        result = stock.peers(self.ticker)
        self.peers = result
        return result

    def get_quote(self, output=None):
        # Vertical
        """1 credit per symbol requested.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'quote'.

        :return: Quote data for the requested symbol.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = stock.quote(self.ticker)

        if output:
            result = self.pandas_singledict_json(result, in_list=False)
            if output == 'csv':
                result.to_csv(filename_builder('.csv', 'quote'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx', 'quote'))

        self.quote = result
        return result

    #       ___                _
    #      / _ \_______ __ _  (_)_ ____ _
    #     / ___/ __/ -_)  ' \/ / // /  ' \
    #    /_/  /_/  \__/_/_/_/_/\_,_/_/_/_/

    def get_price_target(self, output=None):
        """Premium Data. 500 premium credits per symbol requested.
        CSV is formatted vertically with keys in the first column.
        Sets class attribute 'price_target'.

        :return: Latest avg, high, and low analyst price target for a symbol.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = premium.price_target(self.ticker)
        self.price_target = result
        if csv == 'prep':
            self.price_target = self.prep_singledict_json(result, orientation='vertical')
        if csv == 'output':
            self.write_block_to_csv(self.prep_singledict_json(result, orientation='vertical'), 'price_target')
        return result

    def get_analyst_recommendations(self, output=None):
        """Premium Data. 1,000 premium credits per symbol requested.
        Sets class attribute 'analyst_recommendations'.

        :return: Analyst stock recommendations for the requested stock from the last four months.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = premium.recommendation_trends(self.ticker)

        if output:
            result = pandas_listofdict_json(result)
            if output == 'csv':
                result.to_csv(filename_builder('.csv','analyst_recommendations'))
            if output == 'excel':
                result.to_excel(filename_builder('.xlsx','analyst_recommendations'))

        self.analyst_recommendations = result
        return result


    def get_analyst_estimates(self, output=None):
        """Premium Data. 10,000 premium credits per symbol requested.
        Sets class attribute 'analyst_estimates'.
        Not yet implemented.

        :return: Latest consensus estimate for the next fiscal period for the requested symbol.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = premium.future_estimates(self.ticker)
        self.analyst_estimates = result
        return result


    def get_earnings(self, output=None):
        """Premium Data. 1,000 premium credits per symbol requested.
        Earnings are available quarterly (last 4 quarters) and annually (last 4 years).
        Sets class attribute 'earnings'.
        Not yet implemented.

        :return: Earnings data for a given company including the actual EPS, consensus, and fiscal period.


        :param output: Determines the output of the data. Default is raw JSON.
        :type output: accepted values are ['dataframe', 'csv', 'excel'], optional
        """
        result = premium.earnings(self.ticker)
        self.earnings = result
        return result

##### UNPICKLER METHOD #####
def unpickle_class_state(file):
    """This method unpickles/loads pickled class states.
    It will actually load any sort of pickled file, as it's just opening and calling pickle.load() on a file.

    :param file: The file containing the object you would like to unpickle.
    :type file: string, required
    """
    with open(file, 'rb') as f:
        pickle.load(f)
##### UNPICKLER METHOD #####


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
        Sets a class attribute equal to the symbol requested.

        Class attribute 'available_economic_symbols' is a dictionary of available economic symbols and their description.
        Class attribute 'available_commodity_symbols' is a dictionary of available commodity symbols and their description

        :return: Various economic and commodity values as a datapoint.

        :param symbol: The symbol of the economic indicator or commodity datapoint requested.
        :type symbol: string, required
        :param **queries: Additional query parameters you want to include as listed in IEX Docs.
        :type **queries: key value pair as string
        """
        result = market.generic_data_point(symbol, key, **queries)
        setattr(IEXMarket, symbol, result)
        return result

    def get_all_economic_data(self, output_csv=False):
        """18,000 credits per request per day.
        :return: All available current economic indicator datapoints.

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: boolean, optional
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

        :param output: Determines the output of the data. Default is raw JSON.
        :type output: boolean, optional
        """
        output_data = {}
        for key in self.available_commodity_symbols.keys():
            output_data[key] = market.generic_data_point(key, 'market')
        if output_csv:
            with open(f'{self.date}_commodity_data.csv', 'w+') as f:
                for key, value in output_data.items():
                    f.write(str(key) + ',' + str(value) + '\n')
        return output_data

class symbolsAvailable():
    """Returns symbols available on IEX"""
    def __init__(self):
        self.all_symbols = self.raw_symbols()

    def raw_symbols():
        """100 credits per request made.
        The only default return for this class.
        Simply returns the json dict that IEX supplies through their symbols endpoint.
        :return: Symbol, exchange, name, date, isenabled, type, region, currency, iexId, figi, cik.
        """
        SYMBOL_URL = append_iex_token(prepend_iex_url('ref-data/symbols'))
        return get_iex_json_request(url, vprint=vprint)

    def symbol_cik_dict():
        """This is useful in many applications where having the CIK allows direct access to faw data and filings, such as in EDGAR.
        :return: Dictionary containing a symbol and the corrosponding CIK number.
        """
        output_dict = {}
        for company in self.all_symbols:
            output_dict[company['symbol']] = company['cik']
        setattr(symbolsAvailable, 'symbol_cik_dict', output_dict)
        return output_dict

    def symbol_list():
        """:return: List of all the symbols supported by IEX."""
        output_list = []
        for company in self.all_symbols:
            output_list.append(company['symbol'])
        setattr(symbolsAvailable, 'symbol_list', output_list)
        return output_list
