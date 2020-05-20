import scrapy
import logging
from scrapy.utils.log import configure_logging


#logger = logging.getLogger('mycustomlogger') # custom python logger

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://scrapinghub.com']

    def __init__(self, *args, **kwargs):
        logging.basicConfig(
            filename='log.txt',
            format='%(levelname)s: %(message)s',
            level=logging.INFO
        )
        logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
        #logger.setLevel(logging.WARNING) # set logging level
        super().__init__(*args, **kwargs)

    def parse(self, response):
        #self.logger.info('Parse function called on %s', response.url)
        logger.info('Parse function called on %s', response.url)# using custom logger



