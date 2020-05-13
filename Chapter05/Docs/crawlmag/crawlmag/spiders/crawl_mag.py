import scrapy

class MagSpider(scrapy.Spider):
    name = "magnet"
    start_urls = [
        'http://mag234.com/index/index',
        #'http://mag234.com/index/p2',
    ]

    def parse(self, response):
        for link in response.css('ul.link-list li'):
            names = link.css('span.name::text').getall()
            for magnet in  link.css('li::attr(data-magnet)').getall():
                yield {
                    'magnet': magnet,
                }
        next_page = response.xpath('//ul//a[@aria-label="Next"]').css('a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        '''
            yield {
                'name': names,
                'magnet': magnets,
            }
        '''

