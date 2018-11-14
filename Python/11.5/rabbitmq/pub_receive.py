import pika

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)
connection = pika.BlockingConnection(conn)

channel = connection.channel()

# 这里需要和发送端保持一致（习惯和要求）
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
# 创建临时队列，消费者断开之后自动删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue # 取出临时队列的名字

# 将队列和交换机绑定在一起
channel.queue_bind(exchange='logs',
                   queue=queue_name)

def callback(ch, method, properties, body):
    print('receive %s' % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack = True)

channel.start_consuming()