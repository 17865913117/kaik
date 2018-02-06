import time
import threading
import redis
import signal
import requests
from lxml import etree

start_url = 'http://qianmu.iguye.com/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
DOWNLOAD_NUM = 10
# 下载延迟
DOWNLOAD_DELAY = 0.1
threads = []
# 统计下载链接的数量
download_pages = 0
thread_on = True

r = redis.Redis(password='000000')


def fetch(url):
    '''执行网页的抓取'''
    global download_pages
    r = requests.get(url)
    download_pages += 1
    return r.text.replace('\t', '')


def parse(html):
    # 解析入口页面
    dom = etree.HTML(html)
    # 获取页面中表格每一行的第二列中的超链接
    links = dom.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href')
    # 把这些链接放入待抓取队列
    for link in links:
        # 如果有不规则的链接，补全
        if not link.startswith('http://'):
            link = 'http://qianmu.iguye.com/%s' % link
        if r.sadd('qianmu.seen', link):
            r.rpush('qianmu.queue', link)


def parse_university(html):
    # 解析大学详情页面`

    dom = etree.HTML(html)
    # 先选择出表格的父节点，已减少重复代码
    infobox = dom.xpath('//div[@id="wikiContent"]/div[@class="infobox"]')[0]
    # 选择出表格中的每一行第一列的文本内容
    keys = infobox.xpath('./table/tbody/tr/td[1]//text()')
    # 选择出表格中每一行的第二列节点
    cols = infobox.xpath('./table/tbody/tr/td[2]')
    # 遍历第二列的节点，并取出每一个单元格中的文本内容
    values = [','.join(col.xpath('.//text()')) for col in cols]
    # 最后将第一列第二列中的数据合并成一个字典，组成该大学的信息
    info = dict(zip(keys, values))
    r.lpush('qianmu.items',info)


def downloader(i):
    '''下载器，主要执行下载和解析操作'''
    while thread_on:
        # 从队列中读取一个链接，如果没有，则阻塞
        link = r.lpop('qianmu.queue')
        if link:
            # 下载并解析大学详情网页
            parse_university(fetch(link))
            # 向队列发送任务完成信号
            print('thread-%s remaining queue:%s' %(i,r.llen('qianmu.queue')))
        time.sleep(DOWNLOAD_DELAY)
    print('Thread-%s exit now.' % i)


def signal_handler(signum,frame):
    print('received CTRL+C,wait for exit gracefully...')
    global thread_on
    thread_on = False



if __name__ == '__main__':
    start_time = time.time()
    # 抓取并处理入口页面，提取首页内的大学页面链接
    parse(fetch(start_url))

    for i in range(DOWNLOAD_NUM):
        t = threading.Thread(target=downloader,args=(i+1,))
        t.start()
        threads.append(t)
        print('线程(%s)启动' % t.name)

    signal.signal(signal.SIGINT,signal_handler)
    # 退出线程
    for t in threads:
        t.join()

    print('download %s pages in %.2f s' % (download_pages, time.time() - start_time))
