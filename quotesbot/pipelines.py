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
        ass = 0
        for key, url_item in item.items():
            ass += 1
            # list_name = url_item['url_item']
            index = url_item.index('?')
            list_name = url_item
            file_name = str(ass) + '.jpg'  # 图片名称
            # print 'filename',file_name
            file_path = '%s/%s' % (dir_path, file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path, 'ab') as file_writer:
                conn = requests.get(list_name)  # 下载图片
                file_writer.write(conn.content)
            file_writer.close()
        return item
