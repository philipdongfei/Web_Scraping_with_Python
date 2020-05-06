import re
import requests
from bs4 import BeautifulSoup
from Common_base_class import Website, Content

class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

    def crawl(self):
        """
        Get pages from website home page
        """
        bs = self.getPage(self.site.url)
        if bs is not None:
            targetPages = bs.findAll('a', href=re.compile(self.site.targetPattern))
            for targetPage in targetPages:
                targetPage = targetPage.attrs['href']
                if targetPage not in self.visited:
                    self.visited.append(targetPage)
                    if not self.site.absoluteUrl:
                        targetPage = '{}{}'.format(self.site.url, targetPage)
                    self.parse(targetPage)
        else:
            print('getPage is None!')

if __name__ == '__main__':
    reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)',
                      False, 'h1', 'div.StandardArticleBody_body_1gnLA')
    crawler = Crawler(reuters)
    crawler.crawl()



