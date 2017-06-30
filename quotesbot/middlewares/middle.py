# encoding: utf-8
from scrapy.utils.project import get_project_settings
from fake_useragent import UserAgent
# import random

settings = get_project_settings()
from tools.crawler_xici_ip import GetIP

class ProcessHeaderMidware(object):
    # process request add request info

    def process_request(request, spider):
        # 随机从列表中获得header， 并传给user_agent进行使用

        ua = random.choice(settings.get('USER_AGENT_LIST'))
        spider.logger.info(msg='now entring download midware')
        if ua:
            request.headers['User-Agent'] = ua
            # Add desired logging message here
            spider.logger.info(u'User-Agent is : {} {}'.format(request.headers.get('UserAgent-'), request))
        pass

# class RandomUserAgentMiddleware(object):
#     def __init__(self, crawler):
#         super(RandomUserAgentMiddleware, self).__init__()
#         self.user_agent_list = crawler.settings.get("user_agent_list", [])
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(crawler)
#
#     def process_request(self, request, spider):
#         ua = random.choice(settings.get('USER_AGENT_LIST'))
#         request.headers.setdefault('User-Agent', ua)


class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)
        hja = get_ua()
        request.headers.setdefault('User-Agent', get_ua())
        # request.meta["proxy"] = "http://221.238.67.231:8081"


class RandomProxyMiddleware(object):
    # 动态设置ip代理
    def process_request(self, request, spider):
        get_ip = GetIP()
        request.meta["proxy"] = get_ip.get_random_ip()
