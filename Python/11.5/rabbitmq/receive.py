import pika

credentials = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credentials)

connections = pika.BlockingConnection(conn)

channel = connections.channel()

# rabbitmq 消费端仍然使用此方法创建队列
# 这样做的意思是,保证队列的存在
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('Reveive: %s' % body)

# callback 回调函数, 执行结束后立即执行的另一个函数
# no_ack 是否会告知服务端我是否收到消息，如果是True，对方没有收到消息不会pop出
# 始终在队列等待下次发送
channel.basic_consume(callback,
                     queue='hello',
                     no_ack = True)
print('Receive done!')
# 循环取消息
channel.start_consuming()