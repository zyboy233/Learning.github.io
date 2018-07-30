import re
from urllib.request import Request,urlopen

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}

def down_load(url):
    request = Request(url,headers=headers)
    response = urlopen(request)
    code = response.read().decode()
    # print(code)

    pattern = re.compile(r'<div id="info".*?<p>.*?最新更新.*?<a href="(.*?)">(.*?)</a>',re.S)
    result = pattern.findall(code)
    print(result)
    real_url = url+result[0][0]
    name = result[0][1].replace(' ','_')
    print(real_url,name)

    request = Request(real_url, headers=headers)
    response = urlopen(request)
    code = response.read().decode()
    print(code)

    pattern = re.compile(r'<div class="content_read">.*?<div id="content">(.*?)<script>',re.S)
    result = pattern.findall(code)
    print(result)
    with open('{}.txt'.format(name),'w',encoding='utf-8') as f:
        f.write(result[0].replace('<br/>','').replace('&nbsp;','').replace('\t','').replace(r'</br>','').replace('　　　　',''))
        f.close()


url_list = ['https://www.qu.la/book/24868/','https://www.qu.la/book/746/','https://www.qu.la/book/635/','https://www.qu.la/book/31177/']
for url in url_list:
    down_load(url)