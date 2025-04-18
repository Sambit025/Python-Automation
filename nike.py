#Write a code to scrape and save the text data into a file
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    driver.get("https://www.nike.com/in/")
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/nav/div[1]/div/div[2]/nav/ul/li[4]/a').click()
    time.sleep(1)
    driver.find_element(By.ID,'username').send_keys('pandachiku2004@gmail.com')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div/div/form/div/div[4]/button').click()
    input('Press Enter to close the browser')

main()

