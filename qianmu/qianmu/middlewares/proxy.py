import random
from scrapy.exceptions import NotConfigured


class RandomProxyMiddleware(object):

    def __init__(self, settings):
        self.proxies = settings.getlist('PROXIES')


    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured
        if not crawler.settings.getlist('PROXIES'):
            raise NotConfigured

        return cls(crawler.settings)


    def process_request(self, request, spider):
        # 如果request.meta中没有设置proxy，则从代理池中随机设置座位本次请求的代理
        if 'proxy' not in request.meta:
            request.meta['proxy'] = random.choice(self.proxies)
