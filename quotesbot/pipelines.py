# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
import  requests
from quotesbot import settings


class FengNiao(object):

    def process_item(self, item, spider):
        dir_path = '%s/%s' % (settings.FENGNIAO_STORE, spider.name)  # 存储路径
        # print 'dir_path',dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        for key, url_item in item.items():
            list_name = item['url_item']
            # index = url_item.index('.jpg')
            # ass = url_item[index-9:index]
            file_name = item['pic_name'] + '.jpg'  # 图片名称
            file_path = '%s/%s' % (dir_path, file_name)
            if os.path.exists(file_name):
                continue
            with open(file_path, 'ab') as file_writer:
                conn = requests.get(list_name)  # 下载图片
                file_writer.write(conn.content)
            file_writer.close()
        return item
