import os
import requests

# Simple string comprehension to allow setting of states through environment variables.
# REFACTORED!
def arg_to_bool(string):
    affirmative = ['True','TRUE','true','Yes','YES','yes','On','ON','on']
    if string in affirmative:
        return True
    else:
        return False

# This may not be needed
# REFACTORED
def prepend_iex_url(section, external=False):
    sandboxState = arg_to_bool(os.getenv('SANDBOX'))
    if sandboxState is True:
        url = f'https://sandbox.iexapis.com/stable/{section}/'
    else:
        url = f'https://cloud.iexapis.com/stable/{section}/'
    return url

def append_iex_token(url, external=False):
    sandboxState = arg_to_bool(os.getenv('SANDBOX'))
    if external:
        # This is where we can pass in a token instead of getting it from the environment
        token = external
        return f"{url}&token={token}"
    else:
        # Default is grab the token and sandbox state from environment variables
        if sandboxState is True:
            token = os.getenv('IEX_SANDBOX_TOKEN')
        else:
            token = os.getenv('IEX_TOKEN')
        return f"{url}&token={token}"

def get_iex_json_request(url, external=False, vprint=False):
    url = append_iex_token(url, external=external)
    if vprint: print(f"Making request: {url}")
    result = requests.get(url)
    if vprint: print(f"Request status code: {result.status_code}")
    if result.status_code != 200:
        raise BaseException(result.text)
    result = result.json()
    return result

def replace_url_var(url, **kwargs):
    for key, value in kwargs.items():
        url = url.replace('{' + key + '}', value)
    return url

class iexCommon():
    """
    A class that wraps all the common methods used in the IEX requests.
    A class is not / was not strictly neccesary at the beginning of this project.
    Adding support for external tokens meant that code was being repeatedly passed as arguments between functions.
    A class means that these attributes can be shared easily, and it offers some streamlining solutions.
    Certain functions can be done away with completely and others can be broken up more.
    It also means that creating new functions for new endpoints is much easier and could be implemented by an end user.

    :param endpoint: The endpoint you want to access. Specifically this must be the exact string used in the url that points to the desired endpoint.
    :type endpoint: String, required
    :param symbol: The symbol for the stock you would like to request data for.
    :type symbol: String, required
    :param external: Whether you want to use environment variables or not for the token and sandbox settings.
    :type external: Boolean or String. Default is False, insert token here to bypass using environment variables.
    """

    def __init__(self, endpoint, symbol, external=False):
        self.url = f'iexapis.com/stable/{section}/{symbol}/{endpoint}?'
        if external not False:
            self.token = external
            self.parse_token_sandbox(self.token)
        else:
            self.sandbox_state = self.get_env_sandbox()
            self.token = self.get_env_token()
        if sandbox_state is True:
            self.url = 'https://sandbox.' + self.url
        else:
            self.url = 'https://cloud.' + self.url

    # Simple string comprehension and conversion for use with environment variable settings
    def arg_to_bool(self, string):
        affirmative = ['True','TRUE','true','Yes','YES','yes','On','ON','on']
        if string in affirmative:
            return True
        else:
            return False

    # Takes a token string and sets the sandbox state accordingly.
    # All IEX tokens use a 'T' as the first char for sandbox tokens
    def parse_token_sandbox(self, token):
        if self.token[0] == 'T':
            setattr(self, 'sandbox_state', True)
        else:
            setattr(self, 'sandbox_state', False)

    # Gets the sandbox state from environment variable string and parses it into a boolean
    def get_env_sandbox(self):
        sandbox_state = self.arg_to_bool(os.getenv('SANDBOX'))
        return sandbox_state

    # Gets the IEX token from environment variables based on whether sandbox state is enabled.
    def get_env_token(self):
        if sandboxState:
            token = os.getenv('IEX_SANDBOX_TOKEN')
        else:
            token = os.getenv('IEX_TOKEN')
        return token

    # Adds query paramters to the url
    def add_query_params_to_url(self, **query_params):
        for key, value in query_params.items():
            self.url += (f"&{key}={value}")
        return self.url

    # Finalizes the url with the appropriate token - method does not determine which token to append
    def append_token_to_url(self):
        url_final = f"{self.url}&token={self.token}"
        return url_final

    def make_iex_request(self):
        pass

    # Step One
    # Execution of class is split into two parts so that changes to the url can be made halfway through
    def pre_execute(self, query_params):
        self.add_query_params_to_url(self, query_params=None)

    # Step Two
    # Final execution step where token is added and request is made.
    def execute(self):
        self.append_token_to_url()
        self.make_iex_request()




# Basic layout of function in pretty much psuedo code
def test_iex_retrieval(symbol, **query_params):
    """DOCUMENTATION"""
    common = iexCommon(url, symbol, external).pre_execute()
    # Any weird params that need to be added into the url can go here using the '?' as a landmark
    common.execute()
