import openai
import wget
import pathlib
import pdfplumber
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

def displayPaperContent(paperContent, page_start=0, page_end=5):
    for page in paperContent[page_start:page_end]:
        print(page.extract_text())
#displayPaperContent(paperContent)
    
def showPaperSummary(paperContent):
    tldr_tag = "\n tl;dr:"
    # openai.organization = 'organization key'
    
    openai.api_key = os.getenv("API_KEY")
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
        with open("summary.txt", "a") as file:
            file.write(generated_text + "\n")
            file.write("\n---\n\n")
        
def main():
    # paperFilePath = "Research article sample.pdf"
    load_dotenv()
    paper_url = "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/fe/ae/nihms-1849852.PMC9805511.pdf"
    paperFilePath = getPaper(paper_url)
    paperFilePath = "./random_paper1.pdf"
    paperContent = pdfplumber.open(paperFilePath).pages
    showPaperSummary(paperContent)

main()
