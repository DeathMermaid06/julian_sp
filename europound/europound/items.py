# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
 


class EuropoundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#def serializerDollar(value):
#    return f"${str(value)}"

#class DollarItem(scrapy.Item):
#    nombre = scrapy.Field()
#    importe = scrapy.Field(serializer=serializerDollar)

#def serializerDollar(value):
#    return f"${str(value)}"

class DollarItem(scrapy.Item):
    nombre = scrapy.Field()
    importe = scrapy.Field()