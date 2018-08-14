import redis

r = redis.StrictRedis(host='127.0.0.1',port=6379)

print(r.rpush('list2','hello world'))
