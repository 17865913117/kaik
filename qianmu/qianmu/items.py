# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UniversityItem(scrapy.Item):
    # 大学信息item

    # 名称
    name = scrapy.Field()
    # 大学排名
    rank = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 州省
    state = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 本科生数量
    undergraduate_num = scrapy.Field()
    # 研究生数量
    postgraduate_num = scrapy.Field()
    # 网址
    website = scrapy.Field()

if __name__ == '__main__':
    u = UniversityItem(name = '哈弗大学', rank = 1)
    u['country'] = '美国'
    u['state'] = '马萨诸塞州'
    print(u)
    print(u['name'])

    # 将会打印出['country',state,'name'] 不包含未设置的字段
    print(u.keys())
    # 打印所有定义过得字段名称
    print(u.fields.keys())
    # 打印出所有的fields及其序列化函数
    print(u.fields)
    # 判断某个item对象是否包含制定字段
    print('undergraduate_num' in u.fields)
    # 判断某个字段是否设置了值
    print('name' in u)
    print('undergraduate_num' in u)

    # 复制另一个Item对象的值
    u2 = UniversityItem(u)
    u2['ubdergraduate_num'] = 2345
    print(u2)
    print(u)

    # 将Item对象转换为字典对象
    u_dict = dict(u)
    print(type(u_dict))
    # 从一个字典对象中创建item对象
    u3 = UniversityItem(u_dict)
    print(u3)

    # 如果设置一个未定义的字段，则会抛出keyError异常
    u4 = UniversityItem({'unknow' : 123})
    print(u4)
