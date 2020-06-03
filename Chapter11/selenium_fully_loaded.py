from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver',
    options=chrome_options)

driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loadedButton'))
    )
finally:
    #print(driver.find_element_by_id('content').text)
    # be used to create selectors, using the find_element WebDriver function
    print(driver.find_element(By.ID, 'content').text)
    driver.close()

