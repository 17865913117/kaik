import random
from urllib.request import _parse_proxy
from scrapy.exceptions import NotConfigured
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
def reform_url(url):
    # 重组url 返回不带用户名和密码的格式
    proxy_type, *_, hostport = _parse_proxy(url)
    return '%s://%s' % (proxy_type, hostport)


class RandomProxyMiddleware(object):
    #
    max_failed = 3

    def __init__(self, settings):
        self.proxies = settings.getlist('PROXIES')
        # 初始化统计信息，一开始失败次数都是0
        self.stats = {}.fromkeys(map(reform_url,self.proxies), 0)


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

    def process_response(self, request, response, spider):
        # 获取当前使用的proxy
        cur_proxy = request.meta['proxy']
        # print('#'*50,cur_proxy)
        # 判断是http code是否大于400 也就意味这相应失败了
        if response.status >= 400:
            # 将该代理的失败次数加1
            self.stats[cur_proxy] += 1
            # 判断该代理的总失败次数是否已经超过最大失败数
            if self.stats[cur_proxy] > self.max_failed:
                print('%s got a %s response' % (cur_proxy, response.status))
                # 从代理池中删除该代理
                # if cur_proxy in self.proxies:
                #     self.proxies.remove(cur_proxy)
                for proxy in self.proxies:
                    if reform_url(proxy) == cur_proxy:
                        self.proxies.remove(proxy)
                        break
                print('%s removed from proxy list' % cur_proxy)
                # 将本次的请求从新设置一个代理并返回
                request.meta['proxy'] = random.choice(self.proxies)
            return request
        return response

    def process_exception(self, request, exception, spider):
        # print('*'*50,request, request.meta['proxy'])
        # print('-'*50,exception)
        cur_proxy = request.meta['proxy']
        # 如果出现的网络超时或者链接被拒绝 则删除该代理
        if cur_proxy in self.proxies:
            self.proxies.remove(cur_proxy)
        print('%s removed from proxy list' % cur_proxy)
        request.meta['proxy'] = random.choice(self.proxies)
        return request

