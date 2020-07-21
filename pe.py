#pip3 install selenium
#sudo apt-get install chromium-chromedriver
from selenium import webdriver
import selenium
from datetime import date
import time

def browse():
    print("Connected to website")
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d-%m-%Y")
    print("d1 =", d1)
    print("Sleeping")
    driver = webdriver.Chrome()
    pelink = "https://www1.nseindia.com/products/content/equities/indices/historical_pepb.htm"
    driver.get(pelink)
    fromDate = driver.find_element_by_xpath('//*[@id="fromDate"]')
    toDate = driver.find_element_by_xpath('//*[@id="toDate"]')
    fromDate.send_keys(d1)
    toDate.send_keys(d1)
    driver.find_element_by_xpath('//*[@id="yield1"]').click()
    driver.find_element_by_xpath('//*[@id="get"]').click()
    time.sleep(5)
         
    

browse()

