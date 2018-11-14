import pika

# 登陆
credentials = pika.PlainCredentials(username='zy',password='123456')
# 远程连接rabbitmq, 保证rabbitmq端口开放,默认端口:15672
conn = pika.ConnectionParameters('192.168.52.101',credentials=credentials)
# 启用对库进行阻塞, 同步操作进行简单的使用
connection = pika.BlockingConnection(conn)

# 声明一个管道
channel = connection.channel()
# 创建一个队列, 设置队列的名字,如果rabbitmq服务器有队列那么就不管, 没有就自动创建
channel.queue_declare(queue='hello')

# 使用默认的交换机发送信息, exchange为空就是使用默认的
channel.basic_publish(exchange="",
                      routing_key="hello",  # queue的名称,也叫路由键了,写明消息发往的队列
                      body='Hello Word!')  # body消息的详细内容
print('Send done ! body = hello world!')
connection.close()