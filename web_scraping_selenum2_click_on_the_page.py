from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('See what\'s new in the second edition.')
'''a> elements that completely
match the text provided'''
print(type(linkElem))
linkElem.click()
