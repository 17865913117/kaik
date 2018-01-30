import requests
from lxml import etree

# 入口页面地址
start_url = 'http://qianmu.iguye.com/2018USNEWS世界大学排名'
# 待抓取页面地址  存的都是url
link_queue = []

def fetch(url):
    # 执行网页的抓取
    r = requests.get(url)
    # 返回抓取的页面内容，并去除页面中的制表符
    return r.text.replace('\t','')

def parse(html):
    # 解析路口页面
    dom = etree.HTML(html)
    # 获得页面中的表格每一行的第二列中的超链接
    links = dom.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href')
    # 把这些链接放入待抓取队列
    link_queue.extend(links)

def parse_university(html):
    # 解析大学详情页面
    dom = etree.HTML(html)
    # 选择出表格的父节点，以减少代码量
    infobox = dom.xpath('//div[@id="wikiContent"]/div[@class="infobox"]')[0]
    # 选择出表格中每一行的第一列中的文本
    keys = infobox.xpath('./table/tbody/tr/td[1]//text()')
    # 选择出表格中每一行的第二列节点
    cols = infobox.xpath('./table/tbody/tr/td[2]')
    # 便利第二列的节点，并去除每一个单元格中的文本
    values = [','.join(col.xpath('.//text()')) for col in cols]
    # 最后，将第一列 第二列中的数据合并成一个字典 组成该大学的信息
    info = dict(zip(keys, values))
    print(info)


if __name__ == '__main__':
    # 抓取并处理路口页面，提取页面内的大学页面链接
    parse(fetch(start_url))

    # 最大请求数
    max_requests = 5
    # 请求计数器
    requests_count = 0

    # 翻转队列 以便先进先出
    link_queue.reverse()
    while link_queue:
        # 获取最前面的一个链接
        link = link_queue.pop()
        requests_count +=1
        # 如果有不规则的链接 则补全
        if requests_count > max_requests:
            break
        if not link.startswith('http://'):
            link = 'http://qianmu.iguye.com/%s' % link
        #     抓取并处理大学详情页面
        parse_university(fetch(link))