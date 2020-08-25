from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox()
browser.implicitly_wait(10)
'''There is a second type of wait that is distinct from explicit wait called implicit wait. By implicitly waiting, WebDriver polls the DOM for a certain duration when trying to find any element. This can be useful when certain elements on the webpage are not available immediately and need some time to load.'''
browser.get('http://inventwithpython.com')

#WebDriverWait(browser,20)
#WebDriverWait(browser).until(document_initialised)
#WebDriverWait(browser).until(lambda d: d.find_element_by_class_name("jumbotron"))
try:
    elem = browser.find_element_by_class_name('jumbotron')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
