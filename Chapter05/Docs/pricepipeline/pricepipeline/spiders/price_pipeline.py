from scrapy.exceptions import DropItem

class PricePipeline:
    vat_factor = 1.15

    def process_item(self, item, spider):
        if item.get('price'):
            if item.get('price_excludes_vat'):
                item['price'] = item['price']*self.vat_factor
            return item
        else:
            raise DropItem("Missing price in %s" % item)


