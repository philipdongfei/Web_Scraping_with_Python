from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('https://www.biography.com/actor/kevin-bacon')
    #html = urlopen('https://www.rottentomatoes.com/celebrity/kevin_bacon')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:

    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.find_all('a'):
        if 'href' in link.attrs:
            print(link.parent)
            print(link.attrs['href'])
            print()



