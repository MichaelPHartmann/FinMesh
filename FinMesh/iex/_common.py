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

    def __init__(self, section, symbol, endpoint, external=False):
        self.url = f'iexapis.com/stable/{section}/{symbol}/{endpoint}?'
        if not external == False:
            self.token = external
            self.parse_token_sandbox(self.token)
        else:
            self.sandbox_state = self.get_env_sandbox()
            self.token = self.get_env_token()
        if self.sandbox_state is True:
            self.url = 'https://sandbox.' + self.url
        else:
            self.url = 'https://cloud.' + self.url

    # Simple string comprehension and conversion for use with environment variable settings
    def arg_to_bool(self, string):
        """Turns a text string into a boolean response, not fancy.

        :param string: The string you would like to convert to boolean.
        :type string: String, required
        """
        affirmative = ['True','TRUE','true','Yes','YES','yes','On','ON','on']
        if string in affirmative:
            return True
        else:
            return False

    # Takes a token string and sets the sandbox state accordingly.
    # All IEX tokens use a 'T' as the first char for sandbox tokens
    def parse_token_sandbox(self, token):
        """Takes a token string and sets the sandbox state accordingly.
        All IEX tokens use a 'T' as the first char of a token to indicate whether it is a sandbox token.
        This method just looks for that T.

        :param token: The token you would like to parse.
        :type token: String, required
        """
        if self.token[0] == 'T':
            setattr(self, 'sandbox_state', True)
        else:
            setattr(self, 'sandbox_state', False)

    # Gets the sandbox state from environment variable string and parses it into a boolean
    def get_env_sandbox(self):
        """Returns a boolean from the environment variable 'SANDBOX'
        When using system level tokens this will determine whether to call the dummy sandbox environment or the production API
        """
        sandbox_state = self.arg_to_bool(os.getenv('SANDBOX'))
        return sandbox_state

    # Gets the IEX token from environment variables based on whether sandbox state is enabled.
    def get_env_token(self):
        """Returns a token from the appropriate environment variable.
        Variable name is either 'IEX_SANDBOX_TOKEN' or 'IEX_TOKEN'
        Whether the sandbox or production token is retrieved is determined by the environment SANDBOX state.
        """
        if self.sandbox_state:
            token = os.getenv('IEX_SANDBOX_TOKEN')
        else:
            token = os.getenv('IEX_TOKEN')
        return token

    def append_subdirectory_to_url(self, *subdir):
        subdirectory_to_add = F"/{subdir}?"
        self.url  = self.url.replace("?", subdirectory_to_add)
        return self.url

    # Adds query paramters to the url
    def append_query_params_to_url(self, **query_params):
        """Appends query parameters onto the target URL.
        Performs operations on the url attribute.
        Returns the URL with query parameters attached to the end.

        :param query_params: Catchall for keyword arguments. Will be appended to url like "&key=value".
        :type query_params: Keyword arguments, required.
        """
        for key, value in query_params.items():
            self.url += (F"&{key}={value}")
        return self.url

    # Finalizes the url with the appropriate token - method does not determine which token to append
    def append_token_to_url(self):
        """Appends the appropriate token to the end of the url.
        If using environment variables this token is chosen depending on sandbox state.
        If token has been supplied in initialization then that exact token is used.
        Sets attribute url_final for class instance.
        Returns the final URL.
        """
        setattr(self, "url_final", f"{self.url}&token={self.token}")
        return self.url_final

    # Make and handle the request to IEX Cloud with verbose error message
    def make_iex_request(self):
        """Performs request to IEX Cloud from the URL defined in url_final.
        If request does not return a 200 response then a verbose error statement is raised.
        Returns JSON object of response.
        """
        response = requests.get(self.url_final)
        if response.status_code != 200:
            error_response = (F"There was an error with the request to IEX!\n"
                            + F"{response.status_code}:{response.reason} in {round(response.elapsed.microseconds/1000000,4)} seconds\n"
                            + F"URL: {response.url}\n"
                            + "Response Content:\n"
                            + F"{response.text}")
            raise Exception(error_response)
        result = response.json()
        return result

    # Step One
    # Execution of class is split into two parts so that changes to the url can be made halfway through
    def pre_execute(self, **query_params):
        self.add_query_params_to_url(self, query_params)

    # Step Two
    # Final execution step where token is added and request is made.
    def execute(self):
        self.append_token_to_url()
        return self.make_iex_request()
