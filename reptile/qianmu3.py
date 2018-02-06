import time
import threading
from queue import Queue
import requests
from lxml import etree

# 入口页面地址
start_url = 'http://qianmu.iguye.com/2018USNEWS世界大学排名'
# 待抓取页面地址  存的都是url
link_queue = Queue()
# 下载器线程数量
DOWNLOADER_NUM = 10
# 线程池
threads = []
# 统计下载链接的数量
download_pages = 0


def fetch(url):
    # 执行网页的抓取
    global download_pages
    r = requests.get(url)
    download_pages += 1
    # 返回抓取的页面内容，并去除页面中的制表符
    return r.text.replace('\t','')


def parse(html):
    # 解析路口页面
    dom = etree.HTML(html)
    # 获得页面中的表格每一行的第二列中的超链接
    links = dom.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href')
    # 把这些链接放入待抓取队列
    for link in links:
        # 如果有不规则的链接，则补全
        if not link.startswith('http://'):
            link = 'http://qianmu.iguye.com/%s' % link
        #     将链接放入下载队列
        link_queue.put(link)


def parse_unversity(html):
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

def downloader():
    # 下载器 主要执行下载和解析操作
    while True:
        # 从队列中读取一个链接，如果没有，则阻塞
        link = link_queue.get()
        # 如果收到的链接是None，则退出循环
        if link is None:
            break
        # 下载并解析大学详情网页
        parse_unversity(fetch(link))
        # 想队列发送任务完成信号
        link_queue.task_done()
        print('remaining queue %s' % link_queue.qsize())

if __name__ == '__main__':
    start_time = time.time()
    # 抓取并处理路口页面，提取页面内的大学页面链接
    parse(fetch(start_url))

    for i in range(DOWNLOADER_NUM):
        t = threading.Thread(target=downloader)
        t.start()
        threads.append(t)
    # 让队列一直阻塞到全部任务完成
    link_queue.join()

    # 向队列内发送DOWNLOADER_NUM
    for i in range(DOWNLOADER_NUM):
        link_queue.put(None)

    # 退出线程
    for t in threads:
        t.join()

    # 计算程序执行消耗的时间
    print('download %s pages in %.2f seconds' % (download_pages, time.time() - start_time))
