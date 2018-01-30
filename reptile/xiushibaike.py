import requests
from lxml import etree

url = requests.get("https://www.qiushibaike.com/text/")

r = etree.HTML(url.text)
userNames = r.xpath('//div[@class="author clearfix"]/a/h2/text()')
comments = r.xpath('//div[@class="content"]/span/text()')
userNama_list = []
for userName in userNames:
    userNama_list.append(userName)
comment_list = []
for comment in comments:
    comment_list.append(comment)
for i in range(len(userNama_list)):
    print("%s:%s" % (userNama_list[i], comment_list[i]))





