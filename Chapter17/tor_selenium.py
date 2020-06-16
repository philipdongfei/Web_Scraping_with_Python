from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--proxy-server=socks5://127.0.0.1:9150")
driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',
                          options=chrome_options)

driver.get('http://icanhazip.com')
print(driver.page_source)
driver.close()

