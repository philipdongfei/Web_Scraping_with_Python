from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path='/usr/bin/chromedriver',
    options=chrome_options
)
driver.get('http://www.pythonscraping.com/')
imgpath = '/tmp/pythonscraping.png'
driver.get_screenshot_as_file(imgpath)
image = Image.open(imgpath)
image.show()
image.close()
print('Screenshot Done')
driver.close()

