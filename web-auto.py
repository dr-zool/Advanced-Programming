import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

DRIVER="geckodriver"
service = Service(executable_path=DRIVER)
browser = webdriver.Firefox(service=service)

browser.get('https://duckduckgo.com')
search_form = browser.find_element("name", "q")
search_form.send_keys('google')
search_form.submit()

#results = browser.find_elements_by_class_name('result')
#print(results[0].text)

print(browser.title)
time.sleep(5)
browser.close()
quit()
