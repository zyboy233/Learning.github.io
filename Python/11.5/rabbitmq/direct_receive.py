import pika
import sys

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)
connection = pika.BlockingConnection(conn)

channel = connection.channel()

channel.exchange_declare(exchange='direct_log',
                         exchange_type='direct')
# 声明临时队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

routing_key = sys.argv[1:]

for item in routing_key:
    channel.queue_bind(exchange='direct_log',
                       queue= queue_name,
                       routing_key=item)

def callback(ch, method, properties, body):
    print('Receive %s: %s' % (method.routing_key,body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()