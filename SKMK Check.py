import requests
from bs4 import BeautifulSoup as bs4

link = 'https://socialclub.rockstargames.com/crew/nyahelloworld/wall'

url = requests.get(link)
content = url.content
page = bs4(content,'lxml')
find = page.find_all('span')
print(find)