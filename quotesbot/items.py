# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst,Join
from scrapy.loader import ItemLoader

class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


def add_fengniao(value):
    return value + "-fengniao"

def return_value(value):
    return value

class FengNiaoItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class FengNiaoUrl(scrapy.Item):
    url_item = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    pic_name = scrapy.Field(
        input_processor=MapCompose(add_fengniao)
    )

    def get_insert_sql(self):
        insert_sql = """
                    insert into fengniao(pic_name, pic_url)
                    VALUES (%s, %s)  
        """
        url_item = ""
        if self["url_item"]:
            url_item = self["url_item"][0]
        params = (self['pic_name'], url_item)
        return insert_sql, params
