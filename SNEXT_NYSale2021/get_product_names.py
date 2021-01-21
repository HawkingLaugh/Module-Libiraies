import requests
from bs4 import BeautifulSoup as bs4

def names():
    fout = open('result.txt', 'w+', encoding='utf-8')
    url = open('SNEXT.html', 'r',encoding='CP932')
    page = bs4(url,'lxml', from_encoding='CP932')
    urls = []
    url = page.find_all('a')
    for i in url:
        urls.append(i)
    # use set() to remove duplicates
    urls = set(urls)
    names = []
    for j in urls:
        url = j.attrs['href']
        names.append(url.split('/')[-2]+'/'+url.split('/')[-1])
    sortnames = sorted(set(names))
    for k in sortnames:
        fout.write(k)
        fout.write('\n')
    return sortnames