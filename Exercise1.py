#Write a code to scrape and save the text data into a file
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_driver():
    #Set options to make browsing easy
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options)
    driver.get("https://www.wikipedia.org/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH,'//*[@id="www-wikipedia-org"]/main/div[1]/h1/span')
    file = open('wiki.txt','w')
    file.write(element.text)
    # return element
    return element.text

print(main())

