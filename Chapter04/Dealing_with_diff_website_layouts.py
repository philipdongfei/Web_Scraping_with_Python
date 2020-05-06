import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.select('div.StoryBodyCompanionColumn div p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)

def scrapeSina(url):
    bs = getPage(url)
    title = bs.find('title').text
    body = bs.find('div', {'class':'article-content clearfix'}).text
    return Content(url, title, body)


if __name__ == '__main__':
    url = 'https://news.sina.com.cn/c/2020-05-05/doc-iircuyvi1363455.shtml'
    content = scrapeSina(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)


    '''

    url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'
    content = scrapeBrookings(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)

    url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
    content = scrapeNYTimes(url)
    print('Title: {}'.format(content.title))
    print('URL: {}\n'.format(content.url))
    print(content.body)
    '''
