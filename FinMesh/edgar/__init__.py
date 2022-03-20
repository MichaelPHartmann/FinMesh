import os
import requests
import xml.etree.ElementTree as ET
import webbrowser

# EDGAR_BASE_URL = "https://www.sec.gov"
# EDGAR_BROWSE_URL = "/cgi-bin/browse-edgar?action=getcompany"
# EDGAR_ARCHIVE_URL = "/Archives/edgar/data/"
# EDGAR_API_BASE = "https://data.sec.gov/"


class edgarFilerNew():
    """
    """
    def __init__(self, ticker, name="webmaster", email="webmaster@sec.gov"):
        self.edgar_reg_base_url = "https://www.sec.gov"
        self.edgar_api_base_url = "https://data.sec.gov"
        self.edgar_archive_url = "/Archives/edgar/data/"
        self.ticker = ticker
        self.request_log = {}
        self.cik = self.get_cik()
        self.user_name = name
        self.user_email = email

    def get_edgar_request(self, url, user_header=True, stream=False):
        """Returns a response object from EDGAR with options for headers and file streaming.
        Throws a verbose error code on non-200 status codes.
        Saves all raw responses in `request_log` class attribute.

        :param url: The url you would like to request.
        :type url: string, required
        :param user_header: If you would like to send
        """
        if user_header == True:
            headers = {
            "User-Agent" : F"{self.user_name} {self.user_email}"
            }
            response = requests.get(url, headers=headers, stream=stream)
        else:
            response = requests.get(url, stream=stream)

        # Handle failed response
        if response.status_code != 200:
            error_response = (F"There was an error with the request to EDAGR!\n"
                            + F"{response.status_code}:{response.reason} in {round(response.elapsed.microseconds/1000000,4)} seconds\n"
                            + F"URL: {response.url}\n"
                            + "Response Content:\n")
                            # + F"{response.text}")
            raise Exception(error_response)
        else:
            return response

    def get_cik(self):
        """Finds the Central Index Key (CIK) for the requested ticker through HTML tree traversal.
        :return: string, CIK
        """
        URL = F"{self.edgar_reg_base_url}/cgi-bin/browse-edgar?action=getcompany&CIK={self.ticker}&output=atom"
        # Make a request to EDGAR
        response = self.get_edgar_request(URL)
        # Create the root for ET
        # SHOULD BE REFACTORED
        root = ET.fromstring(response.text)
        cik = root[1][4].text
        return cik

    def get_accessions(self, count=20, filter=None):
        """Returns most recent accession numbers and document type for the document for the desired company
        If there is no filter set, it sets and attribute called `accession_numbers` with result.
        If there are filters applied, the filters are joined with underscores in this format: `{filters}_accessions`.

        Data comes from the `data.sec.gov/submissions/` endpoint.
        The SEC asks that users do not make more than 10 requests per second.

        :param count: The number of documents to return.
        :type count: int, optional, default 20
        :param filter: Filters results by the requested form type. Accepts multiple values.
        :type filter: list of strings, optional, defualt is None

        :return: dictionary, {accession_number : {form : filing_type,date : filing_date}}
        """
        URL = F"{self.edgar_api_base_url}/submissions/CIK{self.cik}.json"
        # Make the request and handle any errors with verbose Exception
        response = self.get_edgar_request(URL).json()

        # Define elements in the json
        filings = response["filings"]["recent"]
        accessions = filings["accessionNumber"]
        form = filings["form"]
        date = filings["filingDate"]
        source = filings["primaryDocument"]

        accession_numbers = {}
        if filter:
            n = 0
            while length(accession_numbers) < count:
                # try to find the next entry that fits the filter, otherwise break the loop
                try:
                    if form[n] in filter:
                        n += 1
                        accession_numbers[accessions[n]] = {
                        "form" : form[n],
                        "filingDate" : date[n],
                        "primaryDocument" : source[n]
                        }
                except:
                    break
        else:
            # Build a dictionary
            for i in range(count):
                accession_numbers[accessions[i]] = {
                "form" : form[i],
                "filingDate" : date[i],
                "primaryDocument" : source[i]
                }
        if filter:
            # this may create some gross attribute names but we want to be able to create multiple lists of accessions in one class
            setattr(self, F"{filter.join('_')}_accessions", accessions)
        else:
            setattr(self, "accessions", accessions)

        return accession_numbers

    def get_company_concept(self, concept, taxonomy="us-gaap"):
        """Returns all the disclosures from a single company and concept (a taxonomy and tag) into a single JSON file.
        Returns a separate array of facts for each units on measure that the company has chosen to disclose.
        Sets an attribute for the class formatted like `{concept}_{taxonomy}` which allows you to fetch multiple taxonomies of the same concept.

        Data comes from the `data.sec.gov/api/xbrl/companyconcept/` endpoint.
        The SEC asks that users do not make more than 10 requests per second.

        :param concept: The tag or line item you are requesting.
        :type concept: string, required
        :param taxonomy: The reporting taxonomy for the tag you want to access. (us-gaap, ifrs-full, dei, srt)
        :type taxonomy: string, optional, default is us-gaap

        :return: Dictionary of raw JSON data returned by endpoint
        """
        URL = F"{self.edgar_api_base_url}/api/xbrl/companyconcept/CIK{self.cik}/{taxonomy}/{concept}.json"
        # Make the request and handle any errors with verbose Exception
        response = self.get_edgar_request(URL).json()

        # this allows for mutliple lists of the same concept to be fetched with different taxonomys
        setattr(self, F"{concept}_{taxonomy}", response)
        return response

    def get_company_facts(self):
        """Returns all the company concepts data for a company into a single JSON object.
        Sets a class attribute called `company_facts`.

        Data comes from the `data.sec.gov/api/xbrl/companyfacts/` endpoint.
        The SEC asks that users do not make more than 10 requests per second.

        :return: Dictionary of raw JSON returned by the endpoint
        """
        URL = F"{self.edgar_api_base_url}/api/xbrl/companyfacts/CIK{self.cik}.json"
        # Make the request and handle any errors with verbose Exception
        response = self.get_edgar_request(URL).json()

        setattr(self, "company_facts", response)
        return response

    def get_report_raw(self, accession, directory=None):
        """Takes an accession number and streams a text report file to your environment.
        File is named in the following format: `{ticker}_{accession}`.
        You can use the directory argument to specify the directory you would like to save the file in.
        This uses the exact text entered and appends it to the filename allowing for relative file placement.

        :param accession: The accession number for the report you would like to download. Available online or through `get_accessions method`.
        :type accession: string, required
        :param directory: The directory you would like to send the file to.
        :type directory: string, optional

        :return: filename, string
        """
        fixed_accession = accession.replace("-","")
        URL = f"{edgar_reg_base_url}{edgar_archive_url}{self.cik}/{fixed_accession}/{accession}.txt"

        response = self.get_edgar_request(URL, headers=False, stream=True)
        filename = f'{if directoy: directoy else: ""}{self.ticker}_{accession}.txt'
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        return filename
