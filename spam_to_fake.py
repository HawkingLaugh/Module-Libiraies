from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

PATH = 'C:\Program Files (x86)\chromedriver.exe'
chromeOptions = Options()
chromeOptions.add_argument("--disable-popup-blocking")
chromeOptions.add_argument("--lang=en")
# chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(PATH,chrome_options=chromeOptions)

driver.get('https://www.minuteinbox.com/')
mail = driver.find_element_by_id('email').text
name = mail.split('@')[0]
fullname = name.split('.')
first = fullname[0]
sur = fullname[1]

driver.execute_script("window.open('https://www.instagram.com/accounts/emailsignup/');")
try:
    e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[3]/div/label/input'))
    )
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[3]/div/label/input').send_keys(mail)
    driver.find_element_by_name('fullName').send_keys(first+sur)
    driver.find_element_by_name('username').send_keys(name)
    driver.find_element_by_name('password').send_keys('Ab123456')
    driver.find_element_by_name('password').send_keys(Keys.RETURN)
    # birthday
    year = random.randrange(1990,1998)
    f = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
    )
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select').send_keys(year)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button').send_keys(Keys.ENTER)
    driver.switch_to_window(driver.window_handles[0])
finally:
    print('ok')