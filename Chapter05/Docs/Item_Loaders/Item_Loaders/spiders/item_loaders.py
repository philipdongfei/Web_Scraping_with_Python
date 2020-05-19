import scrapy
from scrapy.loader import ItemLoader
from Items_examples.Product import Product


class ItemLoaders(scrapy.Spider):
    name="itemloader"
    start_urls = [
        'http://www.example.com',
    ]


    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)
        l.add_xpath('name', '//div[@class="product_name"]')
        l.add_xpath('name', '//div[@class="product_title"]')
        l.add_xpath('price', '//p[@id="price"]')
        l.add_css('stock', 'p#stock')
        l.add_value('last_updated', 'today') # you can also use little values
        return l.load_item()




