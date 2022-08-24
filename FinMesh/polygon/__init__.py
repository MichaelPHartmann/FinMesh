from . import stocks
from . import options
from . import forex
from . import reference

class polygonStocks:
    def __init__(self, ticker, external=None):
        self.ticker = ticker
        self.external = external
        self.stocks_endpoints = {
        "aggregates" : "/v2/aggs/ticker/{stock_ticker}/range/{multiplier}/{timespan}/{from}/{to}",
        "grouped daily" : "/v2/aggs/grouped/locale/us/market/stocks/{date}",
        "daily open/close" : "/v1/open-close/{stock_ticker}/{date}",
        "previous close" : "/v2/aggs/ticker/{stock_ticker}/prev",
        "trades v3" : "/v3/trades/{stock_ticker}",
        "trades" : "/v2/ticks/stocks/trades/{stock_ticker}/{date}",
        "last trade" : "/v2/last/trade/{stock_ticker}",
        "quotes v3" : "/v3/quotes/{stock_ticker}",
        "quotes v2" : "/v2/ticks/stocks/nbbo/{stock_ticker}/{date}",
        "last quote" : "/v2/last/nbbo/{stock_ticker}",
        "snapshot all" : "/v2/snapshot/locale/us/markets/stocks/tickers",
        "snapshot gain/lose" : "/v2/snapshot/locale/us/markets/stocks/{direction}",
        "snapshot ticker" : "/v2/snapshot/locale/us/markets/stocks/tickers/{stock_ticker}"
        }

    def get_aggregates(multiplier, timespan, from_date, to_date, **query_params):
        result = stocks.aggregates(self.ticker, multiplier, timespan, from_date, to_date, external=self.external, query_params=query_params)
        return result
    get_aggregates.__doc__ = stocks.aggregates.__doc__

    def get_grouped_daily(self, date, **query_params):
        result = stocks.grouped_daily(date, external=self.external, query_params=query_params)
        return result
    get_grouped_daily.__doc__ = stocks.grouped_daily.__doc__

    def get_daily_open_close(self, date, **query_params):
        result = stocks.daily_open_close(self.ticker, date, external=self.external, query_params=query_params)
        return result
    get_daily_open_close.__doc__ = stocks.daily_open_close.__doc__

    def get_previous_close(self, **query_params):
        result = previous_close(self.ticker, external=self.external, query_params=query_params)
        return result
    get_previous_close.__doc__ = stocks.previous_close.__doc__

    def get_trades_v3(self, **query_params):
        result = stocks.trades_v3(self.ticker, external=self.external, query_params=query_params)
        return result
    get_trades_v3.__doc__ = stocks.trades_v3.__doc__

    def get_trades(self, date, **query_params):
        result = stocks.trades(self.ticker, date, external=self.external, query_params=query_params)
        return result
    get_trades.__doc__ = stocks.trades.__doc__

    def get_last_trade(self, **query_params):
        result = stocks.last_trade(self.ticker, external=self.external, query_params=query_params)
        return result
    get_last_trade.__doc__ = stocks.last_trade.__doc__

    def get_quotes_v3(self, **query_params):
        result = stocks.quotes_v3(self.ticker, external=self.external, query_params=query_params)
        return result
    get_quotes_v3.__doc__ = stocks.quotes_v3.__doc__

    def get_quotes_v2(self, **query_params):
        result = stocks.quotes_v2(self.ticker, external=self.external, query_params=query_params)
        return result
    get_quotes_v2.__doc__ = stocks.quotes_v2.__doc__

    def get_last_quote(self, **query_params):
        result = stocks.last_quote(self.ticker, external=self.external, query_params=query_params)
        return result
    get_last_quote.__doc__ = stocks.last_quote.__doc__

    def get_snapshot_all(self, **query_params):
        result = stocks.snapshot_all(external=self.external, query_params=query_params)
        return result
    get_snapshot_all.__doc__ = stocks.snapshot_all.__doc__

    def get_snapshot_gain_lose(self, direction, **query_params):
        result = stocks.snapshot_gain_lose(direction, external=self.external, query_params=query_params)
        return result
    get_snapshot_gain_lose.__doc__ = stocks.snapshot_gain_lose.__doc__

    def get_snapshot_ticker(self, **query_params):
        result = stocks.snapshot_ticker(self.ticker, external=self.external, query_params=query_params)
        return result
    get_snapshot_ticker.__doc__ = stocks.snapshot_ticker.__doc__

    def get_ticker_details(self, **query_params):
        result = stocks.ticker_details(self.ticker, external=self.external, query_params=query_params)
        return result
    get_ticker_details.__doc__ = stocks.ticker_details.__doc__

    def get_stock_splits_v3(self, **query_params):
        result = stocks.stock_splits_v3(external=self.external, query_params=query_params)
        return result
    get_stock_splits_v3.__doc__ = stocks.stock_splits_v3.__doc__

    def get_dividends_v3(self, **query_params):
        result = stocks.dividends_v3(external=self.external, query_params=query_params)
        return result
    get_dividends_v3.__doc__ = stocks.dividends_v3.__doc__

    def get_financials(self, **query_params):
        result = stocks.financials(external=self.external, query_params=query_params)
        return result
    get_financials.__doc__ = stocks.financials.__doc__

class polygonForex:
    def __init__(self, ticker, external=None):
        self.ticker = ticker
        self.external = external
        self.forex_endpoints = {
            "aggregates" : "/v2/aggs/ticker/{forex_ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}",
            "grouped daily" : "/v2/aggs/grouped/locale/global/market/fx/{date}",
            "previous close" : "/v2/aggs/ticker/{forex_ticker}/prev",
            "quotes" : "/v3/quotes/{forex_ticker}",
            "historic ticks" : "/v1/historic/forex/{from_date}/{to_date}/{date}",
            "last pair quote" : "/v1/last_quote/currencies/{from_date}/{to}",
            "conversion" : "/v1/conversion/{from_date}/{to_date}",
            "snapshot all" : "/v2/snapshot/locale/global/markets/forex/tickers",
            "snapshot gain lose" : "/v2/snapshot/locale/global/markets/forex/{direction}",
            "snapshot ticker" : "/v2/snapshot/locale/global/markets/forex/tickers/{ticker}"
        }

    def get_aggregates(self, multiplier, timespan, from_date, to_date, **query_params):
        result = aggregates(self.ticker, multiplier, timespan, from_date, to_date, external=self.external, query_params=query_params)
        return result
    get_aggregates.__doc__ = forex.aggregates.__doc__

    def get_grouped_daily(self, date, **query_params):
        result = forex.grouped_daily(date, external=self.external, query_params=query_params)
        return result
    get_grouped_daily.__doc__ = forex.__doc__

    def get_previous_close(self, **query_params):
        result = forex.previous_close(self.ticker, external=self.external, query_params=query_params)
        return result
    get_previous_close.__doc__ = forex.previous_close.__doc__

    def get_quotes(self, **query_params):
        result = forex.quotes(self.ticker, external=self.external, query_params=query_params)
        return result
    get_quotes.__doc__ = forex.quotes.__doc__

    def get_historic_ticks(self, from_date, to_date, date, **query_params):
        result = forex.historic_ticks(from_date, to_date, date, external=self.external, query_params=query_params)
        return result
    get_historic_ticks.__doc__ = forex.historic_ticks.__doc__

    def get_last_pair_quote(self, from_date, to_date, **query_params):
        result = forex.last_pair_quote(from_date, to_date, external=self.external, query_params=query_params)
        return result
    get_last_pair_quote.__doc__ = forex.last_pair_quote.__doc__

    def get_conversion(self, from_date, to_date, **query_params):
        result = forex.conversion(from_date, to_date, external=self.external, query_params=query_params)
        return result
    get_conversion.__doc__ = forex.conversion.__doc__

    def get_snapshot_gain_lose(self, direction, **query_params):
        result = forex.snapshot_gain_lose(direction, external=self.external, query_params=query_params)
        return result
    get_snapshot_gain_lose.__doc__ = forex.snapshot_gain_lose.__doc__

    def get_snapshot_all(self, **query_params):
        result = forex.snapshot_all(external=self.external, query_params=query_params)
        return result
    get_snapshot_all.__doc__ = forex.snapshot_all.__doc__

    def get_snapshot_ticker(self, **query_params):
        result = forex.snapshot_ticker(forex_ticker, external=self.external, query_params=query_params)
        return result
    get_snapshot_ticker.__doc__ = forex.snapshot_ticker.__doc__


class polygonOptions:
    def __init__ (self, ticker, external=None):
        self.ticker = ticker
        self.external = external
        self.options_endpoints = {
        "aggregates" : "/v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{from}/{to}",
        "daily open/close" : "/v1/open-close/{options_ticker}/{date}",
        "previous close" : "/v2/aggs/ticker/{options_ticker}/prev",
        "trades" : "/v3/trades/{options_ticker}",
        "last trade" : "/v2/last/trade/{options_ticker}",
        "quotes" : "/v3/quotes/{options_ticker}",
        "snapshot options" : "/v3/snapshot/options/{underlyingAsset}/{optionContract}"
        }
        self.options_reference_endpoints = {
        "options contract" : "/v3/reference/options/contracts/{options_ticker}",
        "options contracts" : "/v3/reference/options/contracts",
        }

    def get_aggregates(self, multiplier, timespan, from_date, to_date, **query_params):
        result = options.aggregates(self.ticker, multiplier, timespan, from_date, to_date, external=self.external, query_params=query_params)
        return result
    get_aggregates.__doc__ = options.aggregates.__doc__

    def get_daily_open_close(self, date, **query_params):
        result = options.daily_open_close(self.ticker, date, external=self.external, query_params=query_params)
        return result
    get_daily_open_close.__doc__ = options.daily_open_close.__doc__

    def get_previous_close (self, **query_params):
        result = options.previous_close(self.ticker, external=self.external, query_params=query_params)
        return result
    get_previous_close.__doc__ = options.previous_close.__doc__

    def get_trades (self, **query_params):
        result = options.trades(self.ticker, external=self.external, query_params=query_params)
        return result
    get_trades.__doc__ = options.trades.__doc__

    def get_last_trade (self, **query_params):
        result = options.last_trade(self.ticker, external=self.external, query_params=query_params)
        return result
    get_last_trade.__doc__ = options.last_trade.__doc__

    def get_quotes (self, **query_params):
        result = options.quotes(self.ticker, external=self.external, query_params=query_params)
        return result
    get_quotes.__doc__ = options.quotes.__doc__

    def get_snapshot_options(self, underlying_asset, option_contract, **query_params):
        result = options.snapshot_options(underlying_asset, option_contract, external=self.external, query_params=query_params)
        return result
    get_snapshot_options.__doc__ = options.snapshot_options.__doc__

    def get_options_contract (self, **query_params):
        result = options.options_contract(self.ticker, external=self.external, query_params=query_params)
        return result
    get_options_contract.__doc__ = options.options_contract.__doc__

    def get_options_contracts(self, **query_params):
        result = options.options_contracts(external=self.external, query_params=query_params)
        return result
    get_options_contracts.__doc__ = options.options_contracts.__doc__


class polygonReference:
    def __init__(self, external=None):
        self.external = external
        self.reference_endpoints = {
        "tickers" : "/v3/reference/tickers",
        "ticker news" : "/v2/reference/news",
        "ticker types" : "/v3/reference/tickers/types",
        "market holidays" : "/v1/marketstatus/upcoming",
        "market status" : "/v1/marketstatus/now",
        "conditions" : "/v3/reference/conditions",
        "exchanges" : "/v3/reference/exchanges"
        }

    def get_tickers(self, **query_params):
        result = reference.tickers(external=self.external, query_params=query_params)
        return result
    get_tickers.__doc__ = reference.tickers.__doc__

    def get_ticker_news(self, **query_params):
        result = reference.ticker_news(external=self.external, query_params=query_params)
        return result
    get_ticker_news.__doc__ = reference.ticker_news.__doc__

    def get_ticker_types(self, **query_params):
        result = reference.ticker_types(external=self.external, query_params=query_params)
        return result
    get_ticker_types.__doc__ = reference.ticker_types.__doc__

    def get_market_holidays(self, **query_params):
        result = reference.market_holidays(external=self.external, query_params=query_params)
        return result
    get_market_holidays.__doc__ = reference.market_holidays.__doc__

    def get_market_status(self, **query_params):
        result = reference.market_status(external=self.external, query_params=query_params)
        return result
    get_market_status.__doc__ = reference.market_status.__doc__

    def get_conditions(self, **query_params):
        result = reference.conditions(external=self.external, query_params=query_params)
        return result
    get_conditions.__doc__ = reference.conditions.__doc__

    def get_exchanges(self, **query_params):
        result = reference.exchanges(external=self.external, query_params=query_params)
        return result
    get_exchanges.__doc__ = reference.exchanges.__doc__
