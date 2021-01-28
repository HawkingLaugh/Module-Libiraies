import requests
from bs4 import BeautifulSoup as bs4

def names():
    urls = ['https://liquorpage.com/japanese-craftgin-all-brand/', 'https://liquorpage.com/japanese-craftgin-all-brand/2/']
    names = []
    for i in urls:
        url = requests.get(i)
        content = url.content
        link = bs4(content,'lxml')
        for i in link.find_all('h2'):
            names.append(i.get_text())
        del names[-1]
    return names