class Website:
    """Common base class for all articles/pages"""

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Product(Website):
    """Contains information for scraping a product page"""
    def __init__(self, name, url, titleTag, productNumberTag, priceTag):
        Website.__init__(self, name, url, titleTag)
        self.productNumberTag = productNumberTag
        self.priceTag = priceTag

class Article(Website):
    """Contains information for scraping an article page"""
    def __init__(self, name, url, titleTag, bodyTag, dateTag):
        Website.__init__(self, name, url, titleTag)
        self.bodyTag = bodyTag
        self.dateTag = dateTag


