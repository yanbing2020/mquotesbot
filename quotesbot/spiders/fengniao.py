# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import FengNiaoUrl


class FengNiao(scrapy.Spider):
    name = "fengniao-xpath"
    # http://bbs.fengniao.com/forum/pic/slide_125_9687202_85562512.html
    # http://www.fengniao.com/
    # allowed_domains = 'http://www.fengniao.com/'
    start_urls = [
        'http://bbs.fengniao.com/forum/pic/slide_125_9687202_85562512.html',
    ]

    def parse(self, response):
        # url = response.xpath('.//div[@class="pic-box"]/@src')
        # url2 = response.xpath('.//div[@class="pic-box"]//@src')
        # imgs = response.xpath('.//div[@class="pic-box"]/img/@src')
        img = response.xpath('.//div[@class="pic-box"]/img/@src').extract_first()
        # for img in response.xpath('.//div[@class="pic-box"]/img/@src'):
        url_items = FengNiaoUrl()
        url_items['url_item'] = img
        yield url_items

        next_url = response.xpath('.//div[@class="pictureAreaR"]//@next-url').extract_first()
        # next = response.urljoin(next_url)
        if next_url is not None:
            yield scrapy.Request(response.urljoin(next_url))
