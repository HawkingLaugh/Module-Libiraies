from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files (x86)\chromedriver.exe'
# for browser option settings
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
# chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)

def get_mail():
    driver.get('https://www.minuteinbox.com/')
    mail = driver.find_element_by_id('email')
    return mail.text