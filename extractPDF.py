import requests
from bs4 import BeautifulSoup


def extract(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # for link in soup.findAll('link'):
    links = soup.findAll('link')[0:5]
    for link in links:
        href = link.get('href')
        filename = href.split('/')[-1]
        newLink = "https" + href[3:]
        # print(newLink)
        # print(filename)
        file_path = "database/" + filename
        # print(file_path)
        response2 = requests.get(newLink)
        # print(href)
        pdf = open(file_path, 'wb')
        pdf.write(response2.content)
        pdf.close()
    print("Done")
