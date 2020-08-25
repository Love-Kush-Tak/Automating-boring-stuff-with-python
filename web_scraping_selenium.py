from selenium import webdriver


browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com')
browser1 = webdriver.Chrome()
print(type(browser1))
browser1.get('http://inventwithpython.com')
