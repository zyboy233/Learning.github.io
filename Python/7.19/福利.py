import re
from urllib.request import Request,urlopen

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
def download_seed(base_url):
    url = 'https://dd9871.com/serchinfo_uncensored/topicsbt/topicsbt_{}.htm'.format(base_url)
    request = Request(url,headers=headers)
    response = urlopen(request)
    code = response.read().decode()
    # print(code)

    pattern = re.compile(r"<div class='Po_u_topicCG'.*?<a href='(.*?)'.*?>",re.S)
    result = pattern.findall(code)
    for av_url in result:
        name = ''
        request = Request(av_url, headers=headers)
        response = urlopen(request)
        code = response.read().decode()
        print(code)
        pattern = re.compile(r"<div class='dht_dl_date_content'>.*?'href','(.*?)'.*?'(.*?)'.*?<",re.S)
        result = pattern.findall(code)
        print(result)
        for head,tail in result:
            tail = str(hex(int(tail)))
            real_url = head+tail
            print(real_url)


download_seed(1)