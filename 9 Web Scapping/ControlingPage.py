from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import geckodriver_autoinstaller
import chromedriver_autoinstaller
import time

# Google Chrome
chromedriver_autoinstaller.install()
browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_page')
 
# The selector ->    #ca-viewsource > a > span
# The Search bar Selector ->    #searchform > div > div > div.cdx-text-input.cdx-text-input--has-start-icon.cdx-text-input--status-default.cdx-search-input__text-input > input
# The Search button ->    #searchform > div > button

try:
    # Click Operation
    #elem = browser.find_element(By.CSS_SELECTOR, "#ca-viewsource > a > span")
    #elem.click()
    time.sleep(3)

    # Search Operation
    elem2 = browser.find_element(By.CSS_SELECTOR, "#searchInput")
    elem2.send_keys("open AI")
    time.sleep(7)

    elem3 = browser.find_element(By.CSS_SELECTOR, "#searchform > div > button")
    elem3.click()
    time.sleep(5)

except:
    print("Can not find an element with that name.")

