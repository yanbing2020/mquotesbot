# -*- coding: utf-8 -*-
# 爬取代理ip

import requests
from scrapy.selector import Selector
import MySQLdb


conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="12345678", db="spider", charset="utf8")
cursor = conn.cursor()

def crawler_ips():
    headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    for i in range(1568):
        re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)

        selector = Selector(text=re.text)
        all_trs = selector.css("#ip_list tr")

        ip_list = []
        for tr in all_trs[1:]:
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed = float(speed_str.split("秒")[0])
            all_texts = tr.css("td::text").extract()

            ip = all_texts[0]
            port = all_texts[1]
            proxy_type = all_texts[5]

            ip_list.append(ip, port, proxy_type, speed)
        for ip_info in ip_list:
            cursor.excute(
                "insert proxy_ips(ip, port, speed, proxy_type) VALUES ('{0}', '{1}',{2}, 'HTTP')".format(
                    ip_info[0], ip_info[1], ip_info[3]
                )
            )
        conn.commit()
