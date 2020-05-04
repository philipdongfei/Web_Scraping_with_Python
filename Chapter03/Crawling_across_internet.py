from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import urllib.request as request
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#Retrieves a list of all Internal linkss found on a page
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        try:
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in internalLinks:
                    if(link.attrs['href'].startswith('/')):
                        internalLinks.append(includeUrl+link.attrs['href'])
                    else:
                        internalLinks.append(link.attrs['href'])
        except AttributeError:
            print('This page is missing something! Continuing.')
    return internalLinks

#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        try:
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
        except AttributeError:
            print('This page is missing something! Continuing.')
    return externalLinks

def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The server could not be found!')
    else:
        if html:
            bs = BeautifulSoup(html, 'html.parser')
            externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
            if len(externalLinks) == 0:
                print('No external links, looking around the site for one')
                domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
                internalLinks = getInternalLinks(bs, domain)
                return getRandomExternalLink(internalLinks[random.randint(0,
                                            len(internalLinks)-1)])
            else:
                return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

if __name__ == '__main__':
    proxy_support = request.ProxyHandler({})
    opener = request.build_opener(proxy_support)
    request.install_opener(opener)
    followExternalOnly('http://oreilly.com')


