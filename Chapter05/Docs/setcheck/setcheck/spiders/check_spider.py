import os
import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'

    def __init__(self):
        if os.environ.get('SCRAPY_CHECK'):
            print('setting check')
            pass # Do some scraper adjustments when a check is running

