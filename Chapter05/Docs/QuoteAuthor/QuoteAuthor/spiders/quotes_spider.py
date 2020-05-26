import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']
    '''

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''

    def parse(self, response):
        ##### Error: HttpRequest not follow_all
        #author_page_links = response.css('.author + a')
        #yield from response.follow_all(author_page_links, callback=self.parse_author)
        #####

        ##### Error: HttpRequest not follow_all
        #for href in response.css('.author + a::attr(href)'):
        #    yield response.follow(href, callback=self.parse_author)
        #####
        for href in response.css('.author + a'):
            yield response.follow(href, callback=self.parse_author)

        #pagination_links = response.css('li.next a')
        #yield from response.follow_all(pagination_links, self.parse)
        pagination_links = response.css('li.next a::attr(href)').get()
        if pagination_links is not None:
            yield response.follow(pagination_links, callback=self.parse)

    def parse_author(self, response):
        # parse item here
        self.state['items_count'] = self.state.get('items_count', 0) + 1
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }

