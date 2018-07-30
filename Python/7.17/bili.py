
from urllib.request import urlopen
from urllib.parse import quote
import string,json,time
# url:http://api.bilibili.com/x/web-interface/archive/stat?aid=10001
# {"code":0,"message":"0","ttl":1,"data":{"aid":10001,"view":22760,"danmaku":195,"reply":191,"favorite":173,"coin":21,"share":47,"like":38,"now_rank":0,"his_rank":0,"no_reprint":0,"copyright":2}}
i = 10001
with open('bili.txt', 'a', encoding='utf-8')as f:
    while i>=1000:
        i+=1
        url = 'http://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(i)
        reponse = urlopen(url)
        reponseStr = reponse.read()
        reponseJson = json.loads(reponseStr)
        print(reponseJson)
        time.sleep(0.5)
        if reponseJson['code'] == 0:
            biliList = []
            for index in reponseJson['data'].items():
                biliList.append(str(index)+',')
            biliList.pop()
            biliList.append('\n')
            for j in biliList:
                f.write(str(j))
            time.sleep(0.5)
    f.close()
