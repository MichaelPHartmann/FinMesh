import os
import requests
import xml.etree.ElementTree as ET
import webbrowser
# from bs4 import BeautifulSoup, SoupStrainer
# from nltk.corpus import words
# from ._common import *

# Accession number format: <hash> - <year> - <filing number>
# https://www.sec.gov/Archives/edgar/data/<cik>/<cik><year+filingNumber>/<primaryDocument>
# https://www.sec.gov/edgar/sec-api-documentation

EDGAR_BASE_URL = "https://www.sec.gov"
EDGAR_BROWSE_URL = "/cgi-bin/browse-edgar?action=getcompany"
EDGAR_ARCHIVE_URL = "/Archives/edgar/data/"

EDGAR_API_BASE = "https://data.sec.gov/"

class edgarFilerNew():
    """
    """
    def __init__(self, ticker):
        self.edgar_reg_base_url = "https://www.sec.gov"
        self.edgar_api_base_url = "https://data.sec.gov"
        self.edgar_archive_url = "/Archives/edgar/data/"
        self.ticker = ticker
        self.cik = self.get_cik()

    def get_edgar_request(self, url, headers=None):

        headers = {
        "User-Agent" : "FinMesh Michael michaelpeterhartmann94@gmail.com",
        # "Accept-Encoding" : "gzip, deflate",
        # "Host" : "www.sec.gov"
        }

        response = requests.get(url, headers=headers)

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
        Sets attribute `accession_numbers` with result.

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
        setattr(self, "accessions", accessions)

        return accession_numbers

    def get_company_concept(self, concept, taxonomy="us-gaap"):
        """Returns all the disclosures from a single company and concept (a taxonomy and tag) into a single JSON file.
        Returns a separate array of facts for each units on measure that the company has chosen to disclose.

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

        setattr(self, "company_concept", response)
        return response

    def get_company_facts(self):
        """Returns all the company concepts data for a company into a single JSON object.

        Data comes from the `data.sec.gov/api/xbrl/companyfacts/` endpoint.
        The SEC asks that users do not make more than 10 requests per second.

        :return: Dictionary of raw JSON returned by the endpoint
        """
        URL = F"{self.edgar_api_base_url}/api/xbrl/companyfacts/CIK{self.cik}.json"
        # Make the request and handle any errors with verbose Exception
        response = self.get_edgar_request(URL).json()

        setattr(self, "company_facts", response)
        return response

#
#
#
#
# class edgarFiler(object):
#     """
#     A class designed for retrieving SEC reports.
#     Currently only supports requests for raw reports, and does not take care of parsing.
#     This class may be useful if you are looking for the CIK number of a company.
#     This attribute is set upon initialization.
#     """
#
#     def __init__(self, ticker):
#         self.ticker = ticker
#         self.cik = self.cik()
#
#     def cik(self):
#         """Sets the CIK attribute for the requested company"""
#         URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&output=atom"
#         search = requests.get(URL)
#         search_result = search.text
#         root = ET.fromstring(search_result)
#         cik = root[1][4].text
#         return cik
#
#     # # # # # # # # # # # # # # # # # # # # # # #
#     # FULL SERVICE ACCESSION AND REPORT GETTING #
#     # # # # # # # # # # # # # # # # # # # # # # #
#     def get_report_full(self, count, document, get=False, html=False, xbrl=False, xlsx=False,debug=False):
#         """
#         Returns accession numbers and documents in five forms for all the documents for the desired company.
#         SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.
#
#         :param count: The number of documents to return.
#         :type count: int, required
#         :param document: The name of the document you wish to request (i.e. '10-K')
#         :type document: string, required
#         :param get: Streams a raw text document for the filings staright to your local workspace.
#         :type get: boolean, optional
#         :param html: Returns an html-only version of the raw text document (parsed by switching at html tags)
#         :type html: boolean, optional
#         :param xbrl: Opens a new web page with the interactive xbrl data.
#         :type xbrl: boolean, optional
#         :param xlsx: Downloads the company-supplied xlsx filing document if available
#         :type xlsx: boolean, optional
#         """
#         document = document_type_parse(document)
#         URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type={document}&count={count}&output=atom"
#
#         get_result = requests.get(URL)
#         if get_result.status_code == 200:
#             result_text = get_result.text
#
#             root = ET.fromstring(result_text)
#
#             accessions_requested = []
#             i = 0
#             for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
#
#                 while i < count:
#                     i += 1
#                     nunber = result.text
#                     accessions_requested.append(nunber)
#
#         else:
#             raise Exception(f'{document} is not a valid document type!')
#
#         # Optionally, one can request the raw text document streamed to your local workspace
#         if get:
#             for accession in accessions_requested:
#                 fixed_accession = accession.replace("-","")
#                 URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
#                 # Stream site to local file
#                 response = requests.get(URL, stream=True)
#                 filename = f'{self.ticker}_{accession}.txt'
#                 with open(filename, 'wb') as f:
#                     for chunk in response.iter_content(chunk_size=512):
#                         if chunk:  # filter out keep-alive new chunks
#                             f.write(chunk)
#
#                 # Optionally, one can request an html-only version of the raw text document (parsed by switching at html tags)
#                 if html:
#                     raw_file = filename
#                     html_file = f"{self.ticker}_{accession}.html"
#                     edgar_strip_to_html(raw_file, html_file)
#
#                 # Optionally, one can request a new web page with the interactive xbrl data
#                 elif xbrl:
#                     URL = f"https://www.sec.gov/cgi-bin/viewer?action=view&amp;cik={self.cik}&amp;accession_number={accession}"
#                     xbrl_request = requests.get(URL)
#                     if xbrl_request.status_code == 200:
#                         webbrowser.open(URL)
#                     else:
#                         raise Exception('Please ensure there are valid CIK and accession numbers.')
#
#                 # Optionally, one can request a download of the xlsx filing document if valid
#                 elif xlsx:
#                     URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/Financial_Report.xlsx"
#                     xlsx_filename = f"{self.ticker}_{accession}.xlsx"
#                     xlsx_download = requests.get(URL)
#                     if xlsx_download.status_code == 200:
#                         with open(xlsx_filename, 'wb') as f:
#                             for chunk in xlsx_download.iter_content(chunk_size=512):
#                                 if chunk:  # filter out keep-alive new chunks
#                                     f.write(chunk)
#                     else:
#                         raise Exception('Please ensure there are valid CIK and accession numbers.')
#
#     return accessions_requested
#
#
#     # # # # # # # # # # # # # # #
#     # GET REPORT FROM ACCESSION #
#     # # # # # # # # # # # # # # #
#     def get_reports(self, accession, get=False, html=False, xbrl=False, xlsx=False,debug=False):
#         """Returns document in five forms for the requested accession number.
#         SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.
#
#         :param accession: The accession number of the report you wish to retrieve
#         :type accession: string, required
#         :param get: Streams a raw text document for the filings staright to your local workspace.
#         :type get: boolean, optional
#         :param html: Returns an html-only version of the raw text document (parsed by switching at html tags)
#         :type html: boolean, optional
#         :param xbrl: Opens a new web page with the interactive xbrl data.
#         :type xbrl: boolean, optional
#         :param xlsx: Downloads the company-supplied xlsx filing document if available
#         :type xlsx: boolean, optional
#         """
#         fixed_accession = accession.replace("-","")
#         URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
#
#         # Stream raw filing to local file
#         response = requests.get(URL, stream=True)
#         filename = f'{self.ticker}_{accession}.txt'
#         with open(filename, 'wb') as f:
#             for chunk in response.iter_content(chunk_size=512):
#                 if chunk:  # filter out keep-alive new chunks
#                     f.write(chunk)
#
#         # Optionally, one can request an html-only version of the raw text document (parsed by switching at html tags)
#         if html:
#             raw_file = filename
#             html_file = f"{self.ticker}_{accession}.html"
#             edgar_strip_to_html(raw_file, html_file)
#
#         # Optionally, one can request a new web page with the interactive xbrl data
#         elif xbrl:
#             URL = f"https://www.sec.gov/cgi-bin/viewer?action=view&amp;cik={self.cik}&amp;accession_number={accession}"
#             xbrl_request = requests.get(URL)
#             if xbrl_request.status_code == 200:
#                 webbrowser.open(URL)
#             else:
#                 raise Exception('Please ensure there are valid CIK and accession numbers.')
#
#         # Optionally, one can request a download of the xlsx filing document if valid
#         elif xlsx:
#             URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/Financial_Report.xlsx"
#             xlsx_filename = f"{self.ticker}_{accession}.xlsx"
#             xlsx_download = requests.get(URL)
#             if xlsx_download.status_code == 200:
#                 with open(xlsx_filename, 'wb') as f:
#                     for chunk in xlsx_download.iter_content(chunk_size=512):
#                         if chunk:  # filter out keep-alive new chunks
#                             f.write(chunk)
#             else:
#                 raise Exception('Please ensure there are valid CIK and accession numbers.')
#
#         return filename
#
#     #
#     # # # # # # # # # # # # # # # # # #
#     # # GET LIST OF ACCESSION NUMBERS #
#     # # # # # # # # # # # # # # # # # #
#     # def get_accessions(self, count, document):
#     #     """Returns accession numbers for the document for the desired company
#     #     SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.
#     #
#     #     :param count: The number of documents to return.
#     #     :type count: int, required
#     #     :param document: The name of the document you wish to request (i.e. '10-K')
#     #     :type document: string, required
#     #     """
#     #     document = document_type_parse(document)
#     #     URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type={document}&count={count}&output=atom"
#     #     # Make the request and handle any errors with verbose Exception
#     #     get_result = requests.get(URL)
#     #     if get_result.status_code != 200:
#     #         error_response = (F"There was an error with the request to EDGAR!\n"
#     #                         + F"{response.status_code}:{response.reason} in {round(response.elapsed.microseconds/1000000,4)} seconds\n"
#     #                         + F"URL: {response.url}\n"
#     #                         + "Response Content:\n"
#     #                         + F"{response.text}")
#     #         raise Exception(error_response)
#     #     else:
#     #         result_text = response.text
#     #
#     #     # Define elements in the page and loop to look for accession numbers
#     #     root = ET.fromstring(result_text)
#     #     accessions_requested = []
#     #     i = 0
#     #     for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
#     #         while i < count:
#     #             i += 1
#     #             nunber = result.text
#     #             accessions_requested.append(nunber)
#     #
#     #     return accessions_requested
#     #
