# -*- coding: utf-8 -*-
import scrapy


class UniversitySpider(scrapy.Spider):
    name = 'university'
    allowed_domains = ['qianmu.iguye.com']
    start_urls = ['http://qianmu.iguye.com/2018USNEWS世界大学排名']

    def parse(self, response):
        # 获得页面中的表格每一行的第二列中的超链接
        links = response.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href').extract()
        # 把这些链接放入带抓取队列中
        for link in links:
            # 如果有不规则的链接，则补全
            if not link.startswith('http://'):
                link = 'http://qianmu.iguye.com/%s' % link
            print(link)
