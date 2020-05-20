import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes_ex'

    def __init__(self, *args, **kwargs):
        self.timeout = int(kwargs.pop('timeout', '60'))
        super(QuotesSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        from twisted.internet import reactor
        reactor.callLater(self.timeout, self.stop)

        urls = ['http://quotes.toscrape.com/page/1']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'text': quote.css('span.text::text').get()}

    def stop(self):
        self.crawler.engine.close_spider(self, 'timeout')


