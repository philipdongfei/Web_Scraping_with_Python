from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find_all(lambda tag: len(tag.attrs) == 2))
print()
print(bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?'))
print()
print(bs.find_all('', text='Or maybe he\'s only resting?'))


