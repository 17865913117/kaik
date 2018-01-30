# import requests
# from lxml import etree
#
# r = requests.get('http://pip.iguye.com/m.htm')
# s = etree.HTML(r.text)
# # 获取每个评论节点
# comments = s.xpath('//div[@class="comment"]')
# # print(comments)
# for comment in comments:
#     # 获取当前评论的用户名称
#     username = comment.xpath('./h3/span[2]/a/text()')[0]
#     # 获取当前评论的内容
#     content = comment.xpath('./p/text()')[0]
#     # 获取评论打分
#     stars = comment.xpath('./h3/span[2]/span[2]/@class')[0]
#     # 获取发表时间
#     comment_time = comment.xpath('./h3/span[2]/span[3]/@title')
#     comment_time = comment_time[0] if comment_time else ''
#     print('%s %s %s: \n%s' % (username,stars, comment_time, content))



import requests
from lxml import etree

headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.8",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': "ll=\"108288\"; bid=f4uVVgcs030; __yadk_uid=Asq2vsVipBeze8x9cXfHHYkXQMcKAemc; ct=y; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1517216131%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DJQnLKRfP2tXBnNVn4gj9Ar0qaT96zLuzESCaCYa237sye5Pu8O3igUc8DKp5x2NQ%26wd%3D%26eqid%3Dfd83a50800009d4a000000025a6ed2f0%22%5D; ps=y; dbcl2=\"158143616:Yj5/Je8pHrk\"; ck=M6b9; _vwo_uuid_v2=E5462F9F8392D231AF286F6BADAB6DFC|2c3786139089c8c94f7de20f3cec6bbe; _pk_id.100001.4cf6=28a9f66c43085309.1517212407.2.1517218138.1517214040.; _pk_ses.100001.4cf6=*; __utma=30149280.533502987.1517212403.1517212403.1517216144.2; __utmb=30149280.2.10.1517216144; __utmc=30149280; __utmz=30149280.1517216144.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.15814; __utma=223695111.1419821432.1517212403.1517212403.1517216144.2; __utmb=223695111.0.10.1517216144; __utmc=223695111; __utmz=223695111.1517216144.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; push_noty_num=0; push_doumail_num=0; ap=1",
    'Host': "movie.douban.com",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
    }


r = requests.get('https://movie.douban.com/subject/26611804/comments',headers = headers)
s = etree.HTML(r.text)
# 获取每个评论节点
comments = s.xpath('//div[@class="comment"]')
# print(comments)
for comment in comments:
    # 获取当前评论的用户名称
    username = comment.xpath('./h3/span[2]/a/text()')[0]
    # 获取当前评论的内容
    content = comment.xpath('./p/text()')[0]
    # 获取评论打分
    stars = comment.xpath('./h3/span[2]/span[2]/@class')[0]
    # 获取发表时间
    comment_time = comment.xpath('./h3/span[2]/span[3]/@title')
    comment_time = comment_time[0] if comment_time else ''
    print('%s %s %s: \n%s' % (username,stars, comment_time, content))
