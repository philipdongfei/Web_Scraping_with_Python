from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    sitemap_url = ['http://www.example.com/sitemap.xml']

    def parse(self, response):
        pass # ... scrape item here ...

