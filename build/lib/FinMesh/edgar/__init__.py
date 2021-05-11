import os
import requests
import xml.etree.ElementTree as ET
import webbrowser
import shutil
from bs4 import BeautifulSoup, SoupStrainer
from nltk.corpus import words
from ._common import *

EDGAR_BASE_URL = "https://www.sec.gov"
EDGAR_BROWSE_URL = "/cgi-bin/browse-edgar?action=getcompany"
EDGAR_ARCHIVE_URL = "/Archives/edgar/data/"

class edgarReport(object):

    def __init__(self,ticker,file):
        self.ticker = ticker
        self.file = file
        self.report_period = ''
        self.company_name = ''

    # WORD FREQUENCY #

    def real_word_frequency(self):
        # Returns a list fo real words sorted by use frequency
        with open(self.file,'r') as f:
            word_list = words.words()
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            file_words = []
            # Quick sieve that is used in bad_apples function to quickly throw out obvious unreal words
            ignore = ['-','_','/','=',':',';','<','>','#','$','@','*','\\']
            lines = f.readlines()
            word_freq = {}
            final_checked = {}
            # Iterate lines from file
            for line in lines:
                words = line.lower().strip().split(' ')
                # Iterate words from line
                for word in words:
                    if not pick_bad_apples(word, ignore):
                        file_words.append(word)
            # Iterate words that pass bad apple check
            for w in file_words:
                if not w == '':
                    length = len(w)-1
                    # Checks if the first and last letter are in the alphabet
                    if w[0] and w[length] in alphabet:
                        w.replace('.','').strip('\"')
                        if w in word_freq.keys():
                            word_freq[w] += 1
                        else:
                            word_freq[w] = 1

            # Runs a final check against an actual dictionary
            for key in word_freq.keys():
                if key in word_list:
                    val = word_freq.get(key)
                    final_checked[key] = val

            # Sort the words by frequency
            final_checked_sorted = {k: v for k, v in sorted(final_checked.items(), key=lambda item: item[1])}

            return final_checked_sorted
    real_word_frequency.__doc__='Returns a list fo real words sorted by use frequency.'

    # RAW REPORT CONVERSION #

    def raw_to_text(self):
        # Converts a raw txt SEC submission to a text-only document
        filein = self.file
        # Open the original file and soupify it
        with open(filein, 'r') as f:
            filein = filein.strip('.txt')
            soup = BeautifulSoup(f, features="html.parser")
            result = soup.get_text()
        # Open the temporary file and writeout the pretty soup
        tempfile = f"{filein}_temp.txt"
        with open(tempfile, 'w+') as tf:
            tf.write(result)
        # Open the temporary file after it has been written to
        with open(tempfile, 'r') as tf:
            lines = tf.readlines()
            # Open the final file and writeout nonblank lines
            newfile = f"{filein}_textonly.txt"
            with open(newfile, "a") as nf:
                for line in lines:
                    if line.strip():
                        nf.write(line)
        # Remove the temporary file
        os.remove(tempfile)
        return newfile

class edgarFiler(object):

    def __init__(self, ticker):
        self.ticker = ticker
        self.cik = self.cik()
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
        return cik
    cik.__doc__='Sets the CIK attribute for the requested company.'


    def accessions(self, count, documents, get=False, html=False, xbrl=False, xlsx=False, strip=False,debug=False):
        # Returns accession numbers and documents in five forms for all the documents for the desired company
        documents_requested = documents.split(' ')
        if debug:
            print(documents_requested)
        # Creates a list of accession numbers for the documents requested.
        # SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.
        for document in documents_requested:
            document = document_type_parse(document)
            URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type={document}&count={count}&output=atom"
            if debug:
                print(URL)
            get_result = requests.get(URL)
            if get_result.status_code == 200:
                result_text = get_result.text
                if debug:
                    print(result_text)
                root = ET.fromstring(result_text)
                if debug:
                    print(root.text)
                accessions_requested = []
                i = 0
                for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
                    if debug:
                        print(result)
                    while i < count:
                        i += 1
                        nunber = result.text
                        accessions_requested.append(nunber)
                        if debug:
                            print(nunber)
            else:
                raise Exception(f'{document} is not a valid document type!')
            if debug:
                print(accessions_requested)

            # Optionally, one can request the raw text document streamed to your local workspace
            if get:
                for accession in accessions_requested:
                    fixed_accession = accession.replace("-","")
                    URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
                    # Stream site to local file
                    response = requests.get(URL, stream=True)
                    filename = f'{self.ticker}_{accession}.txt'
                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=512):
                            if chunk:  # filter out keep-alive new chunks
                                f.write(chunk)

                    # Optionally, one can request an html-only version of the raw text document (parsed by switching at html tags)
                    if html:
                        raw_file = filename
                        html_file = f"{self.ticker}_{accession}.html"
                        edgar_strip_to_html(raw_file, html_file)

                    # Optionally, one can request a new web page with the interactive xbrl data
                    elif xbrl:
                        URL = f"https://www.sec.gov/cgi-bin/viewer?action=view&amp;cik={self.cik}&amp;accession_number={accession}"
                        xbrl_request = requests.get(URL)
                        if xbrl_request.status_code == 200:
                            webbrowser.open(URL)
                        else:
                            raise Exception('Please ensure there are valid CIK and accession numbers.')

                    # Optionally, one can request a download of the xlsx filing document if valid
                    elif xlsx:
                        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/Financial_Report.xlsx"
                        xlsx_filename = f"{self.ticker}_{accession}.xlsx"
                        xlsx_download = requests.get(URL)
                        if xlsx_download.status_code == 200:
                            with open(xlsx_filename, 'wb') as f:
                                for chunk in xlsx_download.iter_content(chunk_size=512):
                                    if chunk:  # filter out keep-alive new chunks
                                        f.write(chunk)
                        else:
                            raise Exception('Please ensure there are valid CIK and accession numbers.')

                    # Optionally, one can request the text-only, stripped down version of the document
                    if strip:
                        raw_to_text(filename)
        return accessions_requested
    accessions.__doc__='Returns accession numbers and documents in five forms for all the documents for the desired company.'

    # # # # # # # # # # #
    # Specific Requests #
    # # # # # # # # # # #

    def accession_requests(self, count, document, debug=False):
        ## Returns accession numbers for the requested document.
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type={document}&count={count}&output=atom"
        get_result = requests.get(URL)
        accessions = []
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
                    accessions.append(nunber)
            return accessions
        else:
            raise Exception('Must enter valid document type!')
    accession_requests.__doc__='Returns accession numbers for the requested document.'

    def accession_10k(self, count, get=False):
        ## Returns accession numbers for all the 10-Ks for the desired company
        ## Will return minimum 10 values
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type=10-k&count={count}&output=atom"
        get_result = requests.get(URL)
        result_text = get_result.text
        root = ET.fromstring(result_text)

        for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
            nunber = result.text
            self.latest_10k_accession.append(nunber)

        if get is True:
            download_report_file(self.latest_10k_accession[:count])
    accession_10k.__doc__='Returns accession numbers for all the 10-Ks for the desired company.'

    def accession_10q(self, count, get=False):
        ## Returns accession numbers for all the 10-Qs for the desired company
        ## Will return minimum 10 values
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&type=10-q&count={count}&output=atom"
        get_result = requests.get(URL)
        result_text = get_result.text
        root = ET.fromstring(result_text)

        for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
            nunber = result.text
            self.latest_10q_accession.append(nunber)

        if get is True:
            download_report_file(self.latest_10q_accession[:count])
    accession_10q.__doc__='Returns accession numbers for all the 10-Qs for the desired company.'

    def accession_all_recent(self, count, get=False):
        ## Returns all the most recent accession numbers for the desired company
        ## Will return minimum 10 values
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&count={count}&output=atom"
        get_result = requests.get(URL)
        result_text = get_result.text
        root = ET.fromstring(result_text)

        for result in root.iter('{http://www.w3.org/2005/Atom}accession-nunber'):
            nunber = result.text
            self.latest_all_accession.append(nunber)

        if get is True:
            download_report_file(self.latest_all_accession[:count])
    accession_all_recent.__doc__='Returns all the most recent accession numbers for the desired company.'


    # # # # # # # # # # # # #
    # RETRIEVAL OF RAW URLS #
    # # # # # # # # # # # # #

    def retrieve_txt_report(self, accession, save=False, classify=False):
        ## Saves the raw xml filing for the given accession number.
        fixed_accession = accession.replace("-","")
        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
        # Stream site to local file
        response = requests.get(URL, stream=True)
        filename = f'{self.ticker}_{accession}.txt'
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=512):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        # Set the file as a class variable, this allows us to modify and use it later
        if save is True:
            var_name = accession
            setattr(edgarFiler, var_name, result)
        else:
            pass
        # Return an edgarReport object instead of just the file name
        if classify is True:
            filename = edgarReport(self.ticker)
            return filename
        else:
            return filename
    retrieve_txt_report.__doc__='Saves the raw xml filing for the given accession number.'

    def retrieve_html_report(self, accession, save=False, open=False):
        ## Strips non-html elements from the raw filing document.
        raw_file = f"{self.ticker}_{accession}.txt"
        html_file = f"{self.ticker}_{accession}.html"
        # If the file is already present, it is converted to pure html
        if os.path.isfile(raw_file):
            edgar_strip_to_html(raw_file, html_file)
        # If the file does not exist it is created and then converted
        else:
            fixed_accession = accession.replace("-","")
            URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"
            # Stream site to local file
            response = requests.get(URL, stream=True)
            filename = f'{self.ticker}_{accession}.txt'
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=512):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
            edgar_strip_to_html(raw_file, html_file)
        # Set the file as a class variable, this allows us to modify and use it later
        if save is True:
            var_name = accession
            setattr(edgarFiler, var_name, result)
        else:
            pass

        if open is True:
            return html_file, webbrowser.open('file://' + html_file)
        else:
            return html_file
    retrieve_html_report.__doc__='Strips non-html elements from the raw filing document.'

    # # # # # # # # # # # #
    # FILE/SITE RETRIEVAL #
    # # # # # # # # # # # #

    def retrieve_xbrl_report(self, accession, save=False):
        ## Opens a browser to the Inline XBRL Interactive report.
        URL = f"https://www.sec.gov/cgi-bin/viewer?action=view&amp;cik={self.cik}&amp;accession_number={accession}"
        xbrl_request = requests.get(URL)
        if xbrl_request.status_code == 200:
            webbrowser.open(URL)
        else:
            raise Exception('Please ensure there are valid CIK and accession numbers.')
    retrieve_xbrl_report.__doc__='Opens a browser to the Inline XBRL Interactive report.'

    def retrieve_xlsx_report(self, accession):
        ## Streams financial statement Excel file, may only work on statements in the last 10 years
        fixed_accession = accession.replace("-","")
        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/Financial_Report.xlsx"
        filename = f"{self.ticker}_{accession}.xlsx"
        xlsx_download = requests.get(URL)
        if xlsx_download.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in xlsx_download.iter_content(chunk_size=512):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
        else:
            raise Exception('Please ensure there are valid CIK and accession numbers.')
    retrieve_xlsx_report.__doc__='Streams financial statement Excel file, may only work on statements in the last 10 years.'
