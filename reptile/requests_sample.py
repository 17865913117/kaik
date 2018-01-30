import requests

params =  {
    'name' : '小明',
    'age' : 2,
    }
print('GET请求')
r = requests.get('http://httpbin.org/get',
                 params=params,
                 headers={
                     'User-Agent' : 'xxxxxxxxxx',
                     'Referer' : 'http://httpbin.org',
                 })
print(r.text)


print('POST请求')
r = requests.post('http://httpbin.org/post' , data=params)
print(r.json())


print('带Cookies请求')
cookies = {'sessionid' :'1234', 'token' : 'xxxxxxxxxxxx'}
r = requests.get('http://httpbin.org/cookies', cookies = cookies)
print(r.text)


print('Session会话保持')
s = requests.Session()
params = {
    'userid' : '123456',
    'token' : 'fhdgskllkdsgklfdhshdlhk'
}
# 先用session对象请求一个url，该url会返回两个cookies
s.get('http://httpbin.org/cookies/set',params = params)
# 再用session对象请求另一个url，会将刚才的cookies传上去
r = s.get('http://httpbin.org/cookies')
print(r.text)


print("抛出状态码异常")
ok_r = requests.get('http://httpbin.org/status/200')
print(ok_r.status_code)
# 当http code为200时 不会抛出异常
ok_r.raise_for_status()

bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# 当http code 不为200类的code时 会抛出异常
bad_r.raise_for_status()
