from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
from grab_name import names

PATH = 'C:\Program Files (x86)\chromedriver.exe'
# for browser option settings
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
# chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(PATH,options=chromeOptions)

bt = []
name = []
driver.get('https://liquorpage.com/japanese-craftgin-all-brand/')
texts = driver.find_elements_by_tag_name('p')
fout = open('jp_Gin.txt', mode='w+', encoding='UTF-8')
for i in texts:
    if '主なボタニカル' in i.text:
        fout.write(i.text)
        fout.write('\n')
        fout.write('\n')


time.sleep(1)
# driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)
driver.get('https://liquorpage.com/japanese-craftgin-all-brand/2/')
texts = driver.find_elements_by_tag_name('p')
fout = open('jp_Gin.txt', mode='a+', encoding='UTF-8')
for i in texts:
    if '主なボタニカル' in i.text:
        fout.write(i.text)
        fout.write('\n')
        fout.write('\n')

