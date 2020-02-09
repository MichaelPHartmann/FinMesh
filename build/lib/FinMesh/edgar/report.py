import os
import re
from bs4 import BeautifulSoup, SoupStrainer

class edgar_report(object):

    def __init__(self,ticker):
        self.ticker = ticker
        self.

    def raw_to_text(filein):
        ## Converts a raw txt SEC submission to a text-only document
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
            print(len(lines))
            # Open the final file and writeout nonblank lines
            newfile = f"{filein}_textonly.txt"
            with open(newfile, "a") as nf:
                for line in lines:
                    if line.strip():
                        nf.write(line)
        # Remove the temporary file
        os.remove(tempfile)
