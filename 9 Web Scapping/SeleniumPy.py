from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import geckodriver_autoinstaller
import chromedriver_autoinstaller

# Google Chrome
chromedriver_autoinstaller.install()
browser = webdriver.Chrome()
browser.get('https://en.wikipedia.org/wiki/Main_page')
 
#wikipedia selector -> #mp-tfp > table > tbody > tr:nth-child(2) > td > p:nth-child(1)
amir = browser.find_element(By.CSS_SELECTOR, '#mp-tfp > table > tbody > tr:nth-child(2) > td > p:nth-child(1)')
print(amir.text)
elem2 = browser.find_elements(By.TAG_NAME, 'p')
print(len(elem2))
print(elem2[4].text)