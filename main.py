import csv
import requests
import json
from bs4 import BeautifulSoup
import xmltodict
import urllib.request
import xml.etree.ElementTree as ET

URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?from=2023-01-01&format=pdf"

if __name__ == '__main__':
    print("hello world");
    
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # for link in soup.findAll('link'):
    link = soup.find('link')
    print(link.get('href'))


