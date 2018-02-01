import faker

class RandomUserAgentMiddleware(object):

    def __init__(self, settings):
        self.faker = faker.Faker()


    @classmethod
    def from_crawler(cls,crawler):
        # 创建一个中间件并返回
        return cls(crawler.settings)

    def process_request(self, request, spider):
        # 设置request头信息内的User-Agent字段
        request.headers['User-Agent'] = self.faker.user_agent()

    def process_response(self, request, response, spider):
        print(request.headers['User-Agent'])
        return response