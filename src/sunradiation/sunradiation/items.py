# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.exceptions import DropItem
import dblite


class SunRadiationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    elevation = scrapy.Field()
    avg_solar_radiation = scrapy.Field()
    avg_wind_speed = scrapy.Field()
    avg_earth_temperature = scrapy.Field()
    frost = scrapy.Field()
    frost_unit = scrapy.Field()

    def __init__(self):
        self.ds = None



    def open_spider(self, spider):
        self.ds = dblite.open(Product, 'sqlite://db/products.sqlite:items', autocommit=True)

    def close_spider(self, spider):
        self.ds.close()

    def process_item(self, item, spider):
        if isinstance(item, Product):
            try:
                self.ds.put(item)
            except dblite.DuplicateItem:
                raise DropItem("Duplicate item found: %s" % item)
        else:
            raise DropItem("Unknown item type, %s" % type(item))
        return item
