import requests
from bs4 import BeautifulSoup as bs4
import os.path
from os import path

url = input('Input your Link: ')
r = requests.get(url)
content = r.content
soup = bs4(content,'lxml')
texts = soup.find_all('a')
prices = soup.find_all('span', class_='itemPrice')

# encoding = 'utf-8' is for writing out japanaes words

while True:
    filename = input('Input filename: ')
    filename = filename +'.txt'
    if path.exists(filename) == False:
        f = open(filename, 'w+', encoding='utf-8')
        for i in texts:     
            text = i.text
            f.write(text)
            f.write('\n')
        for j in prices:
            price = j.text
            f.write(price)
            f.write('\n')
        break
    else:
        print('File exist, name a new file!')
        continue