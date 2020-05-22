import scrapy
from scrapy.crawler import CrawlerProcess


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


process = CrawlerProcess(settings={
    "FEEDS":{
        "items.json": {"format": "json"},
    },
})

process.crawl(AuthorSpider)
process.start() # the script will block here until the crawling is finished

