import os
import re

def egdar_find_html(string):
    if re.search('<HTML>', string) or re.search('<html>', string):
        return 'Start'
    if re.search('</HTML>', string) or re.search('</html>', string):
        return 'End'

def edgar_strip_txt(file, newfile):
    with open(file, 'r+') as f, open(newfile, 'a') as nf:
        transfer = False
        lines = f.readlines()
        for line in lines:
            status = egdar_find_html(line)
            if status == 'Start':
                transfer = True
            elif status == 'End':
                transfer = False
                nf.write(line)

            if transfer == True:
                nf.write(line)
