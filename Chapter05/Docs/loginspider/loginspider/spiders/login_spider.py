import scrapy

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    #pass
    if response.css('.title::text').get() == "Quotes to Scrape":
        return False
    else:
        return True

class LoginSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        print("Existing settings: %s" % self.settings.attributes.keys())
        return scrapy.FormRequest.from_response(
            response,
            formdata = {'username': 'philip', 'password': '1979416'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        yield {
            'author': response.xpath('//div/span[@itemprop="author"]/text()'),
        }

