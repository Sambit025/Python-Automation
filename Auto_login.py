#Some Websites may block this as they have high security for selenium bots and all so this automation method vary for other sites

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
    driver.get("sig_in_url")
    return driver

def main():
    driver = get_driver()
    time.sleep(1)
    driver.find_element(By.XPATH,'xpath for usernam').send_keys('chiku')
    time.sleep(2)
    driver.find_element(By.XPATH,"xpath for password").send_keys('password' + Keys.RETURN)
    time.sleep(2)
    driver.find_element(By.XPATH,'xpath for any key after logging in').click()
    print(driver.current_url)

print(main())

