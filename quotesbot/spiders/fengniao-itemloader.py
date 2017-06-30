# -*- coding: utf-8 -*-
import scrapy
import os
from quotesbot.items import FengNiaoUrl, FengNiaoItemLoader
from scrapy.loader import ItemLoader


class FengNiao(scrapy.Spider):
    name = "fengniao-itemloader"
    # http://bbs.fengniao.com/forum/pic/slide_125_9687202_85562512.html
    # http://www.fengniao.com/
    # allowed_domains = 'http://www.fengniao.com/'
    start_urls = [
        'http://bbs.fengniao.com/forum/pic/slide_125_9687202_85562512.html',
        # 'http://bbs.fengniao.com/forum/pic/slide_125_9652913_85470651.html',
        # 'http://bbs.fengniao.com/forum/pic/slide_125_9648803_85458191.html',
    ]
    # http: // bbs.fengniao.com / forum / pic / slide_125_9652913_85470669.html

    def parse(self, response):
        url_items = FengNiaoUrl()
        # 通过itemloader 加载item
        item_loader = FengNiaoItemLoader(item=FengNiaoUrl(), response=response)
        item_loader.add_css("url_item", ".pic-box > img::attr(src)")
        item_loader.add_css("pic_name", "title::text")

        url_items = item_loader.load_item()
        yield url_items
        next_url = response.css('.pictureAreaR::attr(next-url)').extract_first()
        if next_url is not None:
            yield scrapy.Request(response.urljoin(next_url))
