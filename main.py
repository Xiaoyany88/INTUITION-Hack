import requests
from bs4 import BeautifulSoup


URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?from=2023-01-01&format=pdf"
file_path = "/database"

if __name__ == '__main__':
    print("hello world");
    
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # for link in soup.findAll('link'):
    link = soup.find('link')
    href = link.get('href')
    print(href)
    open("downloads/articles", "wb").write(href)



