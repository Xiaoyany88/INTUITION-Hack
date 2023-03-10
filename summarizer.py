import openai
import wget
import pathlib
import pdfplumber
from ppt2 import *
import numpy as np
import os

from dotenv import load_dotenv
def configure():
        load_dotenv()


def getPaper(paper_url, filename="random_paper1.pdf"):
    """
    Downloads a paper from it's arxiv page and returns
    the local path to that file.
    """
    downloadedPaper = wget.download(paper_url, filename)    
    downloadedPaperFilePath = pathlib.Path(downloadedPaper)

    return downloadedPaperFilePath

# displays the entirety of text information in the Paper
def displayPaperContent(paperContent, page_start=0, page_end=5):
    for page in paperContent[page_start:page_end]:
        print(page.extract_text())
#displayPaperContent(paperContent)

# displays the summarized version of the Paper, using openai davinci
def showPaperSummary(paperContent, prs):
    tldr_tag = "\n tl;dr:"
    # openai.organization = 'organization key'

    openai.api_key = "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"
    engine_list = openai.Engine.list() # calling the engines available from the openai api 
    for page in paperContent:
        text = page.extract_text() + tldr_tag
        response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.3,
            max_tokens=140,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\n"]
        )
        print(response["choices"][0]["text"])
        generated_text = response["choices"][0]["text"]
        with open("summary.txt", "w") as file:
            if (generated_text == ""):
                continue
            new_slide(prs, generated_text)
            file.write(generated_text + "\n")
            file.write("\n---\n\n")

def summarizer(prs):
    # paperFilePath = "Research article sample.pdf"

    cwd = os.getcwd()
    files = os.listdir(cwd+"/database")

    configure()
    # paper_url = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/fe/ae/nihms-1849852.PMC9805511.pdf"
    # paperFilePath = getPaper(paper_url)
    paperFilePath = "database/" + files[0]
    paperContent = pdfplumber.open(paperFilePath).pages
    showPaperSummary(paperContent, prs)






