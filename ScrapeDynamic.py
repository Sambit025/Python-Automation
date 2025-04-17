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
    driver.get("https://everysecond.io/the-internet")
    return driver

def main():
    driver = get_driver()
    time.sleep(3)
    element = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[3]/div[3]/div')
    # return element
    return element.text

print(main())

