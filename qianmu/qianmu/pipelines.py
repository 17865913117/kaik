# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import redis
from scrapy.exceptions import DropItem


class CheckPipeline(object):
    def process_item(self, item, spider):
        '''
        每个item pipiline组件都必须调用该方法，而且这个方法
        必须返回一个item对象
        或者抛出DropItem异常，被丢弃的item不会在传给之后的pipeline组件处理

        :param item: item对象，被抓取的item
        :param spider: （splider对象），抓取该item的splider
        :return: item对象或DropItem异常
        '''

        # 判断如果没有本科生人数字段，则丢弃该item
        if not item.get('undergraduate_num'):
            raise DropItem('Missing fields in %s' % item['name'])
        # 判断如果没有研究生人数字段，则丢弃该item
        if not item.get('postgraduate_num'):
            raise DropItem('Missing fields in %s' % item['name'])
        if item['country'] != '美国':
            raise DropItem('%s is not a USA' % item['name'])
        return item

class RedisPipeline(object):
    '''将大学名称存入到redis中'''
    def __init__(self):
        self.r = redis.Redis()

    def process_item(self,item,spider):
        self.r.sadd(spider.name,item['name'])
        return item



class MysqlPipeline(object):
    def __init__(self):
        self.conn = None
        self.cur = None


    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='000000',
            db='qianmu',
            charset='utf8'
        )
        # 初始化游标对象
        self.cur = self.conn.cursor()



    def process_item(self,item,spider):
        # cols = item.keys()
        # values = [item[key] for key in cols]
        cols, values = zip(*item.items())
        sql = "INSERT INTO `universities` (%s) VALUES (%s)" % \
            (','.join(cols), ','.join(['%s'] * len(values)))
        self.cur.execute(sql,(item['name'],item['rank'],item['country'],
                              item['state'],item['city'],item['undergraduate_num'],
                              item['postgraduate_num'],item['website']))
        self.conn.commit()
        print('mysql: add %s to universities' % item['name'])
        return item

    def close_spider(self,spider):
        # 关闭mysql连接和游标对象
        self.cur.close()
        self.conn.close()
