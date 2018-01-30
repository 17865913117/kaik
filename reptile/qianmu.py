import requests
from lxml import etree

r = requests.get('http://qianmu.iguye.com/2018USNEWS世界大学排名')
dom = etree.HTML(r.text)
max_requests = 5
requests_count = 0

links = dom.xpath('//div[@id="content"]/table/tbody/tr/td[2]/a/@href')
for link in links:
    requests_count += 1
    if requests_count > max_requests:
        break
    if not link.startswith('http://'):
        link = 'http://qianmu.iguye.com/%s' % link
    print(link)
    r = requests.get(link)
    dom = etree.HTML(r.text.replace('\t',''))
    infobox = dom.xpath('//div[@id="wikiContent"]/div[@class="infobox"]')[0]
    keys = infobox.xpath('./table/tbody/tr/td[1]//text()')
    cols = infobox.xpath('./table/tbody/tr/td[2]')
    values = [','.join(col.xpath('.//text()')) for col in cols]

    info = dict(zip(keys,values))
    # for i in range(len(keys)):
    #     info[keys[i]] = values[i]
    print(info)
print('%s links' % len(links))