
from urllib.request import urlopen
import time
pname = 0
day = 0
while True:
    day +=1
    url = 'https://bing.ioliu.cn/v1?d={}&w=1280'.format(day)

    response = urlopen(url)
    responseStr = response.read()

    pname +=1
    with open('C:/Users/45125/Downloads/Bing_1280/{}.jpg'.format(pname),'wb')as f:
        f.write(responseStr)
        f.close()
    time.sleep(0.5)