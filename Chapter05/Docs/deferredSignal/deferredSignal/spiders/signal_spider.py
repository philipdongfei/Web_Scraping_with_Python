import scrapy

class SignalSpider(scrapy.Spider):
    name = 'signals'
    start_urls = ['http://quotes.toscrape.com/page/1/']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(SignalSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
        return spider

    def item_scraped(self, item):
        # Send the scraped item to the server
        d = treq.post(
            'http://example.com/post',
            json.dumps(item).encode('ascii'),
            headers={b'Content-Type': [b'application/json']}
        )

        # The next item will be scraped only after
        # deferred (d) is fired
        return d


    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }


