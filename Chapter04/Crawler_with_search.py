import requests
import time
from bs4 import BeautifulSoup
from Search_common_base_class import Content, Website


class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')


    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self, topic, site):
        """
        Searches a given website for a given topic and records all pages found
        """
        bs = self.getPage(site.searchUrl + topic)
        try:
            searchResults = bs.select(site.resultListing)
        except AttributeError as e:
            print('resultListing was not found')
        else:
            for result in searchResults:
                try:
                    url = result.select(site.resultUrl)[0].attrs['href']
                except AttributeError as e:
                    print('resultUrl was not found')
                else:
                    # Check to see whether it's a relative or an absolute URL
                    if (site.absoluteUrl):
                        bs = self.getPage(url)
                    else:
                        bs = self.getPage(site.url + url)
                    if bs is None:
                        print('Something was wrong with that page or URL. Skipping!')
                        return
                    title = self.safeGet(bs, site.titleTag)
                    body = self.safeGet(bs, site.bodyTag)
                    if title != '' and body != '':
                        content = Content(topic, title, body, url)
                        content.print()


if __name__ == '__main__':
    crawler = Crawler()
    siteData = [
        ['O\'Reilly Media', 'http://oreilly.com', 'https://ssearch.oreilly.com/?q=','article.product-result', 'p.title a', True, 'h1', 'section#product-description'],
        ['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 'div.search-result-content','h3.search-result-title a', False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
        ['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=','div.list-content article', 'h4.title a', True, 'h1', 'div.post-body'],
    ]
    sites = []
    for row in siteData:
        sites.append(Website(row[0], row[1], row[2],
                             row[3], row[4], row[5], row[6], row[7]))
    topics = ['python', 'data science']
    for topic in topics:
        print('#####'*20)
        print('GETTING INFO ABOUT: ' + topic)
        for targetSite in sites:
            print('targetSite:', targetSite.name)
            crawler.search(topic, targetSite)


