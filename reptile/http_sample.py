import urllib.request
import urllib.parse

print('GET请求')
params = urllib.parse.urlencode({
    'name': '小明',
    'age' : '2' ,
})
url = 'http://httpbin.org/get?%s' % params
with urllib.request.urlopen(url) as f:
    print(f.read().decode('utf-8'))



print('POST请求')
req = urllib.request.Request('http://httpbin.org/post',data=params.encode('utf-8'),method='POST')
req.add_header('User-Agent', 'XXXXXXXX')
req.add_header('Referer' , 'http://httpbin.org')
with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))
    print('f.status = ', f.status)
    print('f.reason = ', f.reason)