import requests
from lxml import etree

r = requests.get('http://httpbin.org/')
selector = etree.HTML(r.text)

links = selector.xpath('//@href')
print(links)