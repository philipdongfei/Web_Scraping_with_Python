from CommonProduct import Product
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

if __name__ == '__main__':
    il = ItemLoader(item=Product())
    il.add_value('name', [u'Welcome to my', u'<strong>website</strong>'])
    il.add_value('price', [u'&euro;', u'<span>1000</span>'])
    item = il.load_item()
    print(item)

    #########ItemLoader objects
    loader = ItemLoader(product=Product())

    loader.context['unit'] = 'cm'
    val = loader.get_value(u'name: foo', TakeFirst(), str.upper, re='name: (.+)')
    #print(val)
    loader.add_value('name', u'Color TV')
    loader.add_value('colours', [u'white', u'blue'])
    loader.add_value('length', u'100')
    loader.add_value('name', u'name: foo', TakeFirst(), re='name: (.+)')
    loader.add_value(None, {'name': u'foo', 'sex': u'male'})
    print(loader.load_item())




