from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re

try:
    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    for link in bs.find('div', {'id':'bodyContent'}).find_all(
            'a',href=re.compile('^(/wiki/)((?!:).)*$')
    ):
        if 'href' in link.attrs:
            print(link.attr['href'])

