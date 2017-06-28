# -*- coding: utf-8 -*-
import scrapy


class proxy360(scrapy.Spider):
    name = "proxyip"
    # allowed_domains = 'http://www.fengniao.com/'
start_urls = [
    'http://bbs.fengniao.com/forum/pic/slide_125_9687202_85562512.html',
    'http://bbs.fengniao.com/forum/pic/slide_125_9652913_85470651.html',
    'http://bbs.fengniao.com/forum/pic/slide_125_9648803_85458191.html',
]
