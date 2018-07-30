import random
from urllib.request import Request,urlopen,ProxyHandler,build_opener

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
]
headers = {
    'User-Agent':random.choice(user_agent_list)
}

ip_list = [
    '121.42.167.160:3128',
    '124.193.85.88:8080',
    '121.43.170.207:3128',
    '220.249.185.178:9999',

]

proxies = {
    'http':random.choice(ip_list)
}
# 这只爬虫目标 以及 用户标识
request = Request('http://www.baidu.com',headers = headers)
# 创建IP代理对象
proxy_handler = ProxyHandler(proxies)
# urlopen不支持http高级函数,cookie,验证,代理等内容
# 如果要使用这些内容,需要使用build_opener对象进行处理
opener = build_opener(proxy_handler)

response = opener.open(request)

print(response.read().decode())
