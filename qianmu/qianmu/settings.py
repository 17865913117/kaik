# -*- coding: utf-8 -*-

# Scrapy settings for qianmu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qianmu'

SPIDER_MODULES = ['qianmu.spiders']
NEWSPIDER_MODULE = 'qianmu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'

# Obey robots.txt rules
# 是否遵循robot协议 如果打开 则会在所有请求开始执勤啊，先打开网站根目录下robots.txt文件
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 请求并发数量 默认是16个
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 请求时间的间隔单位s
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否使用cookie
COOKIES_ENABLED = False

# 使用代理
HTTPPROXY_ENABLED = True
# 自定义代理配置
PROXIES = ['http://user:123@39.107.64.28:8888',
 'http://user:123@47.95.119.53:8888',
 'http://user:123@39.106.184.219:8888',
 'http://user:123@39.106.58.146:8888',
 'http://user:123@39.106.120.185:8888',
 # 'http://39.107.76.189:8888',
 # 'http://39.106.184.183:8888',
 # 'http://47.94.208.121:8888',
 # 'http://39.106.222.65:8888',
 # 'http://47.94.245.38:8888',
 # 'http://39.107.71.196:8888',
 # 'http://39.106.175.21:8888',
 # 'http://47.93.251.238:8888',
 # 'http://47.93.60.71:8888',
 # 'http://47.94.9.237:8888',
 # 'http://39.106.130.227:8888',
 # 'http://47.94.221.119:8888',
 # 'http://101.201.239.58:8888',
 # 'http://39.106.189.255:8888',
 # 'http://47.94.170.11:8888',
 # 'http://39.106.125.78:8888',
 # 'http://47.94.147.154:8888',
 # 'http://101.200.48.236:8888',
 # 'http://101.200.48.236:8888',
 # 'http://59.110.142.11:8888',
 # 'http://39.106.198.33:8888'
]


# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Host': "qianmu.iguye.com",
    # 'If-Modified-Since': "Sun, 07 Jan 2018 16:20:20 GMT",
    # 'If-None-Match': "W/\"5a5248c4-ba82\"",
    'Upgrade-Insecure-Requests': "1",
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'qianmu.middlewares.useragent.RandomUserAgentMiddleware': 543,
   'qianmu.middlewares.proxy.RandomProxyMiddleware': 749,

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'qianmu.pipelines.CheckPipeline': 300,
   # 'qianmu.pipelines.RedisPipeline': 301,
   'qianmu.pipelines.MysqlPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
