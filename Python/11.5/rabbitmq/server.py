import pika

credential = pika.PlainCredentials(username='zy',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credential)
connection = pika.BlockingConnection(conn)

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, prop, body):
    # 收到消息，转换成int类型
    n = int(body)
    print('fib %s' % n)

    # 要处理的任务
    response = fib(n)

    # 发布消息，通知到客户端
    ch.basic_publish(exchange='',
                     routing_key=prop.reply_to,
                     properties=pika.BasicProperties(correlation_id=prop.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request,
                      queue='rpc_queue')

print('awaiting Rpc...')
channel.start_consuming()