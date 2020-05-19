import scrapy
from copy import deepcopy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    tags = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serializer=str)
    discount_expiration_date = scrapy.Field()

class SpecificProduct(Product):
    name = scrapy.Field(Product.field['name'], serializer=my_serializer)


if __name__ == '__main__':
    product = Product(name='Desktop PC', price=1000)
    print(product)
    print(product['name'])
    print(product.get('name'))
    print(product['price'])
    #print(product['last_updated'])
    print(product.get('last_updated', 'not set'))
    #print(product['lala'])
    print(product.get('lala', 'unknown field'))
    print('name' in product)
    print('last_updated' in product)
    print('last_updated' in product.fields)
    print('lala' in product.fields)
    product['last_updated'] = 'today'
    print(product['last_updated'])
    #product['lala'] = 'test' # setting unknown field
    print(product.keys())
    print(product.items())
    product['tags'] = ['love', 'inspirational', 'life', 'humor']
    product2 = product.copy()
    print('product tags:', product.get('tags'))
    print('product2 tags:', product2.get('tags'))
    product3 = deepcopy(product)
    print('product3 tags:', product3.get('tags'))
    product2['tags'].append('books')
    print('product2 tags append books')
    print('product tags:', product.get('tags'))
    print('product2 tags:', product2.get('tags'))
    print('product3 tags:', product3.get('tags'))
    dproduct = dict(product)
    print(dproduct)
    product4 = Product({'name': 'Laptop PC', 'price':1500})
    print(product4)
    #Product({'name': 'Laptop PC', 'lala':1500}) # warning: unknown field  in dict







