import requests
from bs4 import BeautifulSoup


URL = "https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?from=2023-01-01&format=pdf"

if __name__ == '__main__':
    
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    # for link in soup.findAll('link'):
    link = soup.find('link')
    href = link.get('href')
    filename = href.split('/')[-1]
    newLink = "https" + href[3:]
    print(newLink)
    print(filename)
    file_path = "/Users/darren/PycharmProjects/INTUITION-Hack/database/" + filename
    print(file_path)
    response2 = requests.get(newLink)
    print(href)
    pdf = open(file_path, 'wb')
    pdf.write(response2.content)
    pdf.close()
    # print(response2)


    # open_url()
    # add to database directory
    # with open(file_path, 'w') as f:
    #     f.write(href)
        # f.write(response.content)
    print("Done")



