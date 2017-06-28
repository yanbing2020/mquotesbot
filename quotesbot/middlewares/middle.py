# encoding: utf-8
from scrapy.utils.project import get_project_settings
import random

settings = get_project_settings()


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


class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.user_agent_list = crawler.settings.get("user_agent_list", [])

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        ua = random.choice(settings.get('USER_AGENT_LIST'))
        request.headers.setdefault('User-Agent', ua)
