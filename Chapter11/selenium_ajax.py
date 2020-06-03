from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# prepare the option for the chrome driver
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',
                          options=chrome_options)
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
#time.sleep(1)
print(driver.find_element_by_id('content').text)
driver.close()

