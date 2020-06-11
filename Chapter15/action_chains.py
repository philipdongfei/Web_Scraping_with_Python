from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver',
    options=chrome_options
)
driver.get('http://pythonscraping.com/pages/files/form.html')

firstnameField = driver.find_element_by_name('firstname')
lastnameField = driver.find_element_by_name('lastname')
submitButton = driver.find_element_by_id('submit')

### METHOD 1 ###
#firstnameField.send_keys('Philip')
#lastnameField.send_keys('Tung')
#submitButton.click()
#####################

### METHOD 2 ####
actions = ActionChains(driver).click(firstnameField).send_keys('Philip').click(lastnameField).send_keys('Tung').send_keys(Keys.RETURN)
actions.perform()
#####################

print(driver.find_element_by_tag_name('body').text)

driver.close()

