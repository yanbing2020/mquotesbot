# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import FengNiaoUrl


class FengNiao(scrapy.Spider):
    name = "fengniao-css"
    # http://bbs.fengniao.com/forum/pic/slide_125_9687202_85562512.html
    # http://www.fengniao.com/
    # allowed_domains = 'http://www.fengniao.com/'
    start_urls = [
        'http://bbs.fengniao.com/forum/pic/slide_125_9652913_85470669.html',
        'http://bbs.fengniao.com/forum/pic/slide_125_9652913_85470651.html',
        'http://bbs.fengniao.com/forum/pic/slide_125_9648803_85458191.html',
    ]
    # http: // bbs.fengniao.com / forum / pic / slide_125_9652913_85470669.html
    def parse(self, response):
        # url_oitems['url_item'] = response.xpath('.//div[@class="pic-box"]/img/@src').extract_first()
        # url_items['pic_name'] = response.xpath('.//title/text()').extract_first()
        url_items = FengNiaoUrl()

        url_items['url_item'] = response.css('.pic-box > img::attr(src)').extract_first()
        url_items['pic_name'] = response.css('title::text').extract_first()
        yield url_items
        # ('.//div[@class="pictureAreaR"]//@next-url')
        next_url = response.css('.pictureAreaR::attr(next-url)').extract_first()
        # next = response.urljoin(next_url)

        if next_url is not None:
            yield scrapy.Request(response.urljoin(next_url))
