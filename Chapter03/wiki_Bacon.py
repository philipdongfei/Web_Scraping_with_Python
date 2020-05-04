from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])


