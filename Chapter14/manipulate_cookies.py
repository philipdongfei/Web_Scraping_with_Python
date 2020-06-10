from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver',
    options=chrome_options
)
driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)

savedCookies = driver.get_cookies()
print(savedCookies)
print()
driver2 = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver',
    options=chrome_options)

driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedCookies:
    print(cookie)
    driver2.add_cookie(cookie)

print()
driver2.get('http://pythonscraping.com')
driver.implicitly_wait(1)
print(driver2.get_cookies())

