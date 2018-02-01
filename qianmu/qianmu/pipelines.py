# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
from scrapy.exceptions import DropItem


class CheckPipeline(object):

    def process_item(self, item, spider):

        # 每个item pipeline 组件都需要调用该方法，而且这个方法必须返回一个item对象，或者抛出Dropitem异常，被丢弃的item不会再传给之后的pipeline组件处理
        '''

        :param item: Item对象，被抓取的item
        :param spider: (Spider对象)， 抓取该item的spider
        :return: item对象或DropItem异常
        '''

        # 判断如果没有本科人数字段 则丢弃item
        if not item.get('undergraduate_num'):
            raise DropItem('Missing fields in %s' % item['name'])
        # 判断如果没有研究生人数字段 则丢弃item
        if not item.get('postgraduate_num'):
            raise DropItem('Missing fields in %s' % item['name'])

        if item['country'] != '美国':
            raise DropItem('%s is not American university' % item['name'])
        return item


class RedisPipeline(object):
    # 将大学排名存入到Redis中
    def __init__(self):
        self.r = redis.Redis()

    def process_item(self, item ,spider):
        self.r.sadd(spider.name, item['name'])
        return item
