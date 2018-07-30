from urllib.request import urlopen,Request

url = 'http://www.baidu.com'
# 如果直接这样写,等于告诉网页获取网页内容的不是自然人,而是
# 程序,程序自带User-Agent:Python urllib / 3.6
# urlopen()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 替换程序的User-Agent  即用户标识
request = Request(url , headers = headers)
reponse = urlopen(request)
# decode 解码  encode 编码
print(reponse.read().decode())

# 爬虫/反爬流程:
# 1.判断是否是Python urllib,解决办法,伪装User-Agent,进行爬虫
# 2.判断同一个User-Agent是否多次访问,解决办法:换成不同的User-Agent访问
# 3.判断同一个ip是否多次访问,解决办法:使用不同ip访问

