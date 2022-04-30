import os

stocks = {
"aggregates" : "/v2/aggs/ticker/{stockTicker}/range/{multiplier}/{timespan}/{from}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/us/market/stocks/{date}",
"daily open/close" : "/v1/open-close/{stockTicker}/{date}",
"previous close" : "/v2/aggs/ticker/{stockTicker}/prev",
"trades v3" : "/v3/trades/{stockTicker}",
"trades" : "/v2/ticks/stocks/trades/{stockTicker}/{date}",
"last trade" : "/v2/last/trade/{stockTicker}",
"quotes v3" : "/v3/quotes/{stockTicker}",
"quotes v2" : "/v2/ticks/stocks/nbbo/{stockTicker}/{date}",
"last quote" : "/v2/last/nbbo/{stockTicker}",
"snapshot all" : "/v2/snapshot/locale/us/markets/stocks/tickers",
"snapshot gain/lose" : "/v2/snapshot/locale/us/markets/stocks/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/us/markets/stocks/tickers/{stockTicker}"
}

stocks_reference = {
"ticker details" : "/v3/reference/tickers/{stockTicker}",
"stock splits v3" : "/v3/reference/splits",
"dividends v3" : "/v3/reference/dividends",
"financials" : "/vX/reference/financials",
}

options = {
"aggregates" : "/v2/aggs/ticker/{optionsTicker}/range/{multiplier}/{timespan}/{from}/{to}",
"daily open/close" : "/v1/open-close/{optionsTicker}/{date}",
"previous close" : "/v2/aggs/ticker/{optionsTicker}/prev",
"trades" : "/v3/trades/{optionsTicker}",
"last trade" : "/v2/last/trade/{optionsTicker}",
"quotes" : "/v3/quotes/{optionsTicker}",
"snapshot options" : "/v3/snapshot/options/{underlyingAsset}/{optionContract}"
}

options_reference = {
"options contract" : "/v3/reference/options/contracts/{options_ticker}",
"options contracts" : "/v3/reference/options/contracts",
}

forex = {
"aggregates" : "/v2/aggs/ticker/{forexTicker}/range/{multiplier}/{timespan}/{from}/{to}",
"grouped daily" : "/v2/aggs/grouped/locale/global/market/fx/{date}",
"previous close" : "/v2/aggs/ticker/{forexTicker}/prev",
"quotes" : "/v3/quotes/{fxTicker}",
"historic ticks" : "/v1/historic/forex/{from}/{to}/{date}",
"last pair quote" : "/v1/last_quote/currencies/{from}/{to}",
"conversion" : "/v1/conversion/{from}/{to}",
"snapshot all" : "/v2/snapshot/locale/global/markets/forex/tickers",
"snapshot gain lose" : "/v2/snapshot/locale/global/markets/forex/{direction}",
"snapshot ticker" : "/v2/snapshot/locale/global/markets/forex/tickers/{ticker}"
}

reference = {
"tickers" : "/v3/reference/tickers",
"ticker news" : "/v2/reference/news",
"ticker types" : "/v3/reference/tickers/types",
"market holidays" : "/v1/marketstatus/upcoming",
"market status" : "/v1/marketstatus/now",
"conditions" : "/v3/reference/conditions",
"exchanges" : "/v3/reference/exchanges"
}

class polygonCommon():

    def __init__(self, url_extension, external=False):
        self.url = "https://api.polygon.io" + url_extension
        if external:
            self.token = external
        else:
            self.get_env_token()

    def get_env_token(self):
        token = os.getenv('POLYGON_TOKEN')
        setattr(self, "token", token)
        return self.token

    # Adds query paramters to the url
    def append_query_params_to_url(self, query_params):
        """Appends query parameters onto the target URL.
        Performs operations on the url attribute.
        Returns the URL with query parameters attached to the end.

        :param query_params: Catchall for keyword arguments. Will be appended to url like "&key=value".
        :type query_params: Dictionary, required.
        """
        for key, value in query_params.items():
            self.url += (F"&{key}={value}")
        return self.url

    # Finalizes the url with the appropriate token - method does not determine which token to append
    def append_token_to_url(self):
        """Appends the appropriate token to the end of the url.
        If token has been supplied in initialization then that exact token is used.
        Sets attribute url_final for class instance.
        Returns the final URL.
        """
        setattr(self, "url_final", f"{self.url}&token={self.token}")
        return self.url_final

    # Make and handle the request to Polygon.io with verbose error message
    def make_polygon_request(self):
        """Performs request to Polygon.io from the URL defined in url_final.
        If request does not return a 200 response then a verbose error statement is raised.
        Returns JSON object of response.
        """
        response = requests.get(self.url_final)
        if response.status_code != 200:
            error_response = (F"There was an error with the request to Polygon.io!\n"
                            + F"{response.status_code}:{response.reason} in {round(response.elapsed.microseconds/1000000,4)} seconds\n"
                            + F"URL: {response.url}\n"
                            + "Response Content:\n"
                            + F"{response.text}")
            raise Exception(error_response)
        result = response.json()
        return result

    # Final execution step where token is added and request is made.
    def execute(self):
        self.append_token_to_url()
        return self.make_polygon_request()
