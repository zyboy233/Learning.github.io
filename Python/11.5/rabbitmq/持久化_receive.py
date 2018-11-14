import pika

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)
connections = pika.BlockingConnection(conn)

# 建立通道
channel = connections.channel()

channel.queue_declare(queue='task_queue',durable=True)

def callback(ch, method, properties, body):
    print('receive %s' % body)
    # raise NameError
    # 手动对消息进行确认
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 保证能够做完之后通知给server端
channel.basic_qos(prefetch_count=1)

# no_ack 默认值是false， 需要对message进行确认
channel.basic_consume(callback,
                      queue='task_queue')
# 循环接收消息
channel.start_consuming()