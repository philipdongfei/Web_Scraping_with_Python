from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
from urllib.error import HTTPError
from urllib.error import URLError

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    try:
        html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print('The server could not be found!')
        return None
    else:
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


if __name__ == '__main__':
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
