from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author + a'):
            yield response.follow(href, callback=self.parse_author)

        #pagination_links = response.css('li.next a')
        #yield from response.follow_all(pagination_links, self.parse)
        pagination_links = response.css('li.next a::attr(href)').get()
        if pagination_links is not None:
            yield response.follow(pagination_links, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(AuthorSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished


