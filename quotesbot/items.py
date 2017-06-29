# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_fengniao(value):
    return value + "-fengniao"


class FengNiaoItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class FengNiaoUrl(scrapy.Item):
    url_item = scrapy.Field(

    )
    pic_name = scrapy.Field(
        input_processor=MapCompose(add_fengniao)
    )

