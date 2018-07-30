import requests
from bs4 import BeautifulSoup

url = 'http://news.baidu.com/'

response = requests.get(url).content
print(response)
bs4_soup = BeautifulSoup(response,'lxml')
print(bs4_soup)
new_list = bs4_soup.select('ul.focuslistnews li a')
print(new_list)
for news in new_list:
    href = news.get('href')
    text = news.get_text()
    print('新闻:'+ text +'  链接:' + href)