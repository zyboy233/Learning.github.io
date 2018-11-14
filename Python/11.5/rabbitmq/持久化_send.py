import pika
import time

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)
connections = pika.BlockingConnection(conn)

# 创建管道
channel = connections.channel()

# durable: server关闭，队列仍存在
channel.queue_declare(queue='task_queue',durable=True)

message = 'test keep_long'

# deliver_mode=2 消息持久化
num = 1
while num < 10:
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message + str(num),
                          properties=pika.BasicProperties(delivery_mode=2))
    num += 1
    time.sleep(2)
print('Send done! %s' % message)
connections.close()