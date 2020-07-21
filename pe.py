#pip3 install selenium
#sudo apt-get install chromium-chromedriver
from selenium import webdriver
#import details
import constants  
from os import path
import time
driver = webdriver.Chrome()
inputfile = 'title.py'
f = open('output.txt','w')

def browse(sector):   
    print(sector)
    driver.get(sector)
    # time.sleep(2)
    sector_name = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/div/h6').text
    sector_pe = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/div/a/div').text
    sector_name.replace("PE" , "")
    print(sector_name)
    print(sector_name," - " ,sector_pe, file= f)



#NIFTYBANK = details.Ratio(constants.NIFTYBANK , constants.NIFTYBANKLINK)
browse(constants.NIFTYBANKLINK)
browse(constants.NIFTYITLINK)
browse(constants.NIFTYITLINK)

file1 = open(inputfile, 'r')
Lines = file1.readlines()
for line in Lines:
    print(line)


driver.close()

 

