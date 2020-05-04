from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import re

try:
    html = urlopen('https://www.biography.com/actor/kevin-bacon')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find('body', {'class':'^(mm)(.)*$'}).find_all(
            'a',href=re.compile('^(/actor/)(.)*$')
    ):
        try:
            if 'href' in link.attrs:
                print(link.attr['href'])
        except AttributeError as e:
            print('Tag href was not found')


