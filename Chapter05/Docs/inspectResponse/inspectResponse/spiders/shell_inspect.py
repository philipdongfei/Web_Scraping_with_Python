import scrapy

class MySpider(scrapy.Spider):
    name = "scrapyspider"
    start_urls = [
        "https://scrapy.com",
        "https://scrapy.org",
        "https://scrapy.net",
    ]

    def parse(self, response):
        # We want to inspect one specific response.
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)

        # Rest of parsing code.
        yield {"title": response.xpath('//title/text()').get() }


