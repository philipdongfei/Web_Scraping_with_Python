from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1',
                       user='philip', passwd='75356072Philip&%#%^)&@',
                       db='mysql', charset='utf8' )
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES ("%s", "%s")',
                (title, content))
    cur.connection.commit()

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id': 'my-content-text'}).find('p').get_text()
    store(title, content)
    return bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

if __name__ == '__main__':
    links = getLinks('/wiki/Kevin_Bacon')
    try:
        while len(links) > 0:
            newArticle = links[random.randint(0, len(links)-1)].attrs['href']
            print(newArticle)
            links = getLinks(newArticle)
    finally:
        cur.close()
        conn.close()

