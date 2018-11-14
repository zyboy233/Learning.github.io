import pika
import sys

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)
connection = pika.BlockingConnection(conn)

channel = connection.channel()

# 创建一个exchange，direct_log 类型是direct
channel.exchange_declare(exchange='direct_log',
                         exchange_type='direct')

routing_key = sys.argv[1] if len(sys.argv)>1 else 'info'
message = 'log 233'
channel.basic_publish(exchange='direct_log',
                      routing_key=routing_key,
                      body=message)
print('Send %s:%s' % (routing_key,message))
connection.close()