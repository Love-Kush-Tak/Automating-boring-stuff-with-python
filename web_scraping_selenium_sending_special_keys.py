from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
print(htmlElem)
htmlElem.send_keys(Keys.PAGE_DOWN) # scrolls to bottom
#browser.implicitly_wait(20)
#htmlElem.send_keys(Keys.HOME)
