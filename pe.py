#pip3 install selenium
#sudo apt-get install chromium-chromedriver
from selenium import webdriver
import selenium
driver = webdriver.Chrome()
pelink = "https://www1.nseindia.com/products/content/equities/indices/historical_pepb.htm"
driver.get(pelink)

def browse():
    print("Connected to website")


browse()
