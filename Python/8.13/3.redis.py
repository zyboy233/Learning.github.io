import redis
import json,csv
import codecs

r = redis.StrictRedis(host='127.0.0.1',port=6379,charset='GBK')

# for page in range(220,379):
#     print(r.rpush('avspider:start_urls','https://javbooks.com/serchinfo_uncensored/topicsbt/topicsbt_{}.htm'.format(str(page))))

str_list = r.lrange('av:items', 0, -1)
file = open('file.csv','w+',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['name','img','bt'])
for str in str_list:
    str = str.decode('utf-8')
    jsonStr = json.loads(str)
    if jsonStr['name']:
        name = jsonStr['name']
        img = jsonStr['img']
        bt_str = jsonStr['bt_str']
        writer.writerow([name,img,bt_str])
