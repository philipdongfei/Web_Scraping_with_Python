import scrapy

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    #pass
    if response.css('.title::text').get() == u"新浪邮箱":
        return False
    else:
        return True

class LoginSpider(scrapy.Spider):
    name = 'mail_sina'
    start_urls = ['https://mail.sina.com.cn/?from=mail']

    def parse(self, response):
        print("Existing settings: %s" % self.settings.attributes.keys())
        return scrapy.FormRequest.from_response(
            response,
            formdata = {'username': 'dongfei154@sina.com', 'password': '1979416Philip'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        yield {
            'title': response.xpath('//td/span[@title]/text()'),
        }

