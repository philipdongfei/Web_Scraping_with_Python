from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://mag234.com/index/index')
bs = BeautifulSoup(html, 'html.parser')
names = bs.find_all('span', {'class':'name'})
for name in names:
    print(name.get_text())

mags = bs.find_all('li', {'data-id': re.compile('[0-9]+')})
print('mags: ', len(mags))
for mag in mags:
    print(mag['data-magnet'])
    print(mag['data-ed2k'])
    print()
