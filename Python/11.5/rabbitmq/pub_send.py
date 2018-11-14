import pika
import sys

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)
connection = pika.BlockingConnection(conn)

channel = connection.channel()
# 有多个设备去连接到交换机，那么，这个交换机把消息发送给哪个设备，是根据
# 交换机的类型决定的。交换机的类型有：direct，topic，fanout
# fanout 这个类型是所有交换机的设备都收到消息，即广播
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')
print(sys.argv[0])
message = sys.argv[1] if len(sys.argv) > 1 else 'info: logs'

# 将消息发送到名为logs的exchange的交换机中
# 因为是fanout类型，所以不需要指定routing_key
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print('Send %s' % message)
connection.close()