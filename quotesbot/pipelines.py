# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys
import urllib
import requests
from quotesbot import settings
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
class FengNiao(object):

    def process_item(self, item, spider):
        main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # main.py所在文件夹
        dir_path = '%s/%s' % (main_dir, spider.name)  # 存储路径
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


class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        #执行具体的插入
        insert_sql = """
                    insert into fengniao(pic_name, pic_url)
                    VALUES (%s, %s)               
                """
        #根据不同的item 构建不同的sql语句并插入到mysql中
        cursor.execute(insert_sql, (item['pic_name'], item['url_item']))

