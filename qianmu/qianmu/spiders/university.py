# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse

class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['qianmu.iguye.com']
    start_urls = ['http://qianmu.iguye.com/2018USNEWS世界大学排名']

    def  __init__(self, max_num=0,*args,**kwargs):
        super(UniversitySpider, self).__init__(*args, **kwargs)
        self.max_num = int(max_num)


    def parse(self, response):
        # 获得页面中的表格每一行的第二列中的超链接
        # extract将节点转换成一个字符串列表
        links = response.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href').extract()
        # 把这些链接放入带抓取队列
        for i, link in enumerate(links):
            if self.max_num and i >= self.max_num:
                break
            # 如果有不规则的链接，则补全
            if not link.startswith('http://'):
                link = 'http://qianmu.iguye.com/%s' % link
            request = scrapy.Request(link, callback = self.parse_unversity)
            request.meta['rank'] = i + 1
            yield request

    def parse_unversity(self, response):
        # 解析大学详情页面
        # 去除网页内的特殊符号
        response = response.replace(body = response.body.decode('utf-8').replace('\t', ''))
        item = {
            'name' : response.xpath('//h1[@class="wikiTitle"]/text()').extract_first(),
            'rank' : response.meta['rank']
        }
        # 选择出表格的父节点，以减少代码量
        infobox = response.xpath('//div[@id="wikiContent"]/div[@class="infobox"]')[0]
        # 选择出表格中每一行的第一列中的文本
        keys = infobox.xpath('./table/tbody/tr/td[1]//text()').extract()
        # 选择出表格中每一行的第二列节点
        cols = infobox.xpath('./table/tbody/tr/td[2]')
        # 便利第二列的节点，并去除每一个单元格中的文本
        values = [','.join(col.xpath('.//text()').extract()) for col in cols]
        # 最后，将第一列 第二列中的数据合并成一个字典 组成该大学的信息
        item.update(zip(keys, values))
        yield item
        self.logger.info('item %s scraped' % item['name'])
