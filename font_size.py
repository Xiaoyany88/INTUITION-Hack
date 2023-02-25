from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar,LTLine,LAParams
import os

import fitz

def get_title():
    cwd = os.getcwd()
    files = os.listdir(cwd+"/database")


    def scrape(filePath):
        results = [] # list of tuples that store the information as (text, font size, font name)
        pdf = fitz.open(filePath) # filePath is a string that contains the path to the pdf
        for page in pdf:
            dict = page.get_text("dict")
            blocks = dict["blocks"]
            for block in blocks:
                if "lines" in block.keys():
                    spans = block['lines']
                    for span in spans:
                        data = span['spans']
                        for lines in data:
                            results.append((lines['text'], lines['size'], lines['font']))
                                # lines['text'] -> string, lines['size'] -> font size, lines['font'] -> font name
        pdf.close()
        return results

    list = scrape("database/" + files[0])
    i = 1
    title1 = list[0][0]
    while(list[i][1] == list[i-1][1]):
        title1 += list[i][0]
        i += 1

    author = list[i][0]
    i += 1
    while (list[i][1] == list[i - 1][1]):
        title1 += list[i][0]
        i += 1

    # print(title1)
    # print(list)
    return [title1, author]
