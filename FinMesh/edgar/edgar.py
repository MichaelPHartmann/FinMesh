import os
import requests
import xml.etree.ElementTree as ET
import webbrowser
import shutil
from _common import *

EDGAR_BASE_URL = "https://www.sec.gov"
EDGAR_BROWSE_URL = "/cgi-bin/browse-edgar?action=getcompany"
EDGAR_ARCHIVE_URL = "/Archives/edgar/data/"

class edgarFiler(object):

    def __init__(self, ticker):
        self.ticker = ticker
        #self.cik = cik(self.ticker)
        self.latest_10k_accession = []
        self.latest_10q_accession = []
        self.latest_all_accession = []

    def cik(self):
        ## Sets the CIK attribute for the requested company.
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&output=atom"
        search = requests.get(URL)
        search_result = search.text
        root = ET.fromstring(search_result)
        cik = root[1][4].text
        self.cik = cik
        return cik

    # # # # # # # # # # # # # # #
    # GETTING ACCESSION NUMBERS #
    # # # # # # # # # # # # # # #

    def accession_requests(self, count, document):
        ## Will return minimum 10 values.
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type={document}&count={count}&output=atom"
        get_result = requests.get(URL)
        if get_result.status_code == 200:
            result_text = get_result.text
            root = ET.fromstring(result_text)

            for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
                nunber = result.text
                if document == "10-k" or "10-K":
                    self.latest_10k_accession.append(nunber)
                if document == "10-q" or "10-Q":
                    self.latest_10q_accession.append(nunber)
                else:
                    new_list = str(document)
                    setattr(edgarFiler, new_list, [])
                    self.latest_all_accession.append(nunber)
        else:
            raise Exception('Must enter valid document type!')

    def accessions(self, count, documents):
        ## Returns accession numbers for all the documents for the desired company
        ## Will return minimum 10 values.
        documents_requested = documents.split(' ')
        for document in documents_requested:
            URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type={document}&count={count}&output=atom"
            get_result = requests.get(URL)
            if get_result.status_code == 200:
                result_text = get_result.text
                root = ET.fromstring(result_text)

                for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
                    nunber = result.text
                    if document == "10-k" or "10-K":
                        self.latest_10k_accession.append(nunber)
                    if document == "10-q" or "10-Q":
                        self.latest_10q_accession.append(nunber)
                    else:
                        new_list = str(document)
                        setattr(edgarFiler, new_list, [])
                        self.latest_all_accession.append(nunber)
            else:
                raise Exception(f'{document} is not a valid document type!')

    def accession_10k(self, count):
        ## Returns accession numbers for all the 10-Ks for the desired company
        ## Will return minimum 10 values
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type=10-k&count={count}&output=atom"
        get_result = requests.get(URL)
        result_text = get_result.text
        root = ET.fromstring(result_text)

        for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
            nunber = result.text
            self.latest_10k_accession.append(nunber)

    def accession_10q(self, count):
        ## Returns accession numbers for all the 10-Qs for the desired company
        ## Will return minimum 10 values
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type=10-q&count={count}&output=atom"
        get_result = requests.get(URL)
        result_text = get_result.text
        root = ET.fromstring(result_text)

        for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
            nunber = result.text
            self.latest_10q_accession.append(nunber)

    def accession_all_recent(self, count):
        ## Returns all the most recent accession numbers for the desired company
        ## Will return minimum 10 values
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&count={count}&output=atom"
        get_result = requests.get(URL)
        result_text = get_result.text
        root = ET.fromstring(result_text)

        for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
            nunber = result.text
            self.latest_all_accession.append(nunber)

    # # # # # # # # # # # # #
    # RETRIEVAL OF RAW URLS #
    # # # # # # # # # # # # #

    def retrieve_raw_report(self, accession, save=False):
        ## Saves the raw xml filing for the given accession number.
        fixed_accession = accession.replace("-","")
        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
        # Stream site to local file
        with requests.get(URL, stream=True) as result:
            filename = f'{self.ticker}_{accession}.txt'
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        # Set the file as a class variable, this allows us to modify and use it later
        if save is True:
            var_name = accession
            setattr(edgarFiler, var_name, result)
        else:
            pass

        return filename

    def retrieve_html_report(self, accession, save=False):
        ## Strips non-html elements from the raw filing document.
        raw_file = f"{self.ticker}_{accession}.txt"
        html_file = f"{accession}.html"
        # If the file is already present, it is converted to pure html
        if os.path.isfile(raw_file):
            edgar_strip_txt(raw_file, html_file)
        # If the file does not exist it is created and then converted
        else:
            fixed_accession = accession.replace("-","")
            URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
            # Stream site to local file
            with requests.get(URL, stream=True) as result:
                filename = f'{self.ticker}_{accession}.txt'
                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            edgar_strip_txt(raw_file, html_file)
        # Set the file as a class variable, this allows us to modify and use it later
        if save is True:
            var_name = accession
            setattr(edgarFiler, var_name, result)
        else:
            pass

        return html_file

    def retrieve_xbrl_report(self, accession, save=False):
        ## Opens a browser to the Inline XBRL Interactive report.
        URL = f"https://www.sec.gov/cgi-bin/viewer?action=view&amp;cik={self.cik}&amp;accession_number={accession}"
        xbrl_request = requests.get(URL)
        if xbrl_request.status_code == 200:
            webbrowser.open(URL)
        else:
            raise Exception('Please ensure there are valid CIK and accession numbers.')

    def retrieve_xlsx_report(self, accession, save=False):
        ## Opens a browser to trigger a download of the financial statements Excel file.
        """
        The apparent way to do this is to trigger the download by opening a browser window.
        Trying to simply write the 'text' to a new (.xlsx) file returns a corrupted excel file.
        Streaming is an alternative but so far what I have tried still results in corrupted files.
        """
        fixed_accession = accession.replace("-","")
        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/Financial_Report.xlsx"
        xlsx_download = requests.get(URL)
        if xlsx_download.status_code == 200:
            webbrowser.open(URL)
        else:
            raise Exception('Please ensure there are valid CIK and accession numbers.')

    # # # # # # # # # # # #
    # CONVERSION OF FILES #
    # # # # # # # # # # # #

    def convert_to_html(self, filename):
        with open(filename, 'r+') as f:
            print(f.readline(1))

    def convert_to_original(self, filename):
        pass
