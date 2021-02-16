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

class edgarFiler(object):

    def __init__(self, ticker):
        self.ticker = ticker
        self.cik = self.cik()

    def cik(self):
        ## Sets the CIK attribute for the requested company.
        URL = EDGAR_BASE_URL + EDGAR_BROWSE_URL + f"&CIK={self.ticker}&output=atom"
        search = requests.get(URL)
        search_result = search.text
        root = ET.fromstring(search_result)
        cik = root[1][4].text
        return cik
    cik.__doc__='Sets the CIK attribute for the requested company.'

    # # # # # # # # # # # # # # # # # # # # # # #
    # FULL SERVICE ACCESSION AND REPORT GETTING #
    # # # # # # # # # # # # # # # # # # # # # # #
    def get_report_full(self, count, document, get=False, html=False, xbrl=False, xlsx=False,debug=False):
    # Returns accession numbers and documents in five forms for all the documents for the desired company
    # SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.
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

    return accessions_requested
    accessions.__doc__='Returns accession numbers and documents in five forms for all the documents for the desired company.'

    # # # # # # # # # # # # # # #
    # GET REPORT FROM ACCESSION #
    # # # # # # # # # # # # # # #
    def get_reports(self, accession, get=False, html=False, xbrl=False, xlsx=False,debug=False):
    # Returns accession numbers and documents in five forms for all the documents for the desired company
    # SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.

        fixed_accession = accession.replace("-","")
        URL = f"https://www.sec.gov/Archives/edgar/data/{self.cik}/{fixed_accession}/{accession}.txt"

        # Stream raw filing to local file
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

        return filename
    accessions.__doc__='Returns accession numbers and documents in five forms for all the documents for the desired company.'

    # # # # # # # # # # # # # # # # #
    # GET LIST OF ACCESSION NUMBERS #
    # # # # # # # # # # # # # # # # #
    def get_accessions(self, count, document, get=False, html=False, xbrl=False, xlsx=False,debug=False):
    # Returns accession numbers for the document for the desired company
    # SEC lists a minimum of 10 numbers for any given result but that is parred down in this code.
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

    return accessions_requested
    accessions.__doc__='Returns accession numbers and documents in five forms for all the documents for the desired company.'


class edgarReport(object):

    def __init__(self,ticker,file):
        self.ticker = ticker
        self.file = file
        self.report_period = ''
        self.company_name = ''

    def get_report_attributes():
        with open(self.file, 'r') as f:
            text = f.read()
        report_period = "CONFORMED PERIOD OF REPORT:	"
        file_date = "FILED AS OF DATE:		"
        company_name = "COMPANY CONFORMED NAME:			"
        industrial_classification = "STANDARD INDUSTRIAL CLASSIFICATION:	"
        report_period_start = text.find(report_period)+len(report_period)
        file_date_start = text.find(file_date)+len(file_date)
        company_name_start = text.find(company_name)+len(company_name)
        company_name_end =
        industrial_classification_start = text.find(industrial_classification)+len(industrial_classification)
        industrial_classification_end =

    # # # # # # # # # # #
    # Isolating  Tables #
    # # # # # # # # # # #

    def isolate_tables(self, debug=True):
        with open(self.file, 'r') as fo:
            text = fo.read()
        starts, ends = find_all_tables(text)
        if debug: print(starts, ends)
        table_only_output = f'{self.ticker}_{self.report_period}_tablesonly.html'
        with open(table_only_output, 'a') as f:
            for i in range(len(starts)-1):
                block_to_write = text[starts[i]:ends[i]]
                f.write(block_to_write)
    isolate_tables.__doc__='Isolates all the tables in a SEC filing to a new file.'


    # # # # # # # # # #
    # WORD  FREQUENCY #
    # # # # # # # # # #

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
