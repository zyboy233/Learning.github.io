import pika
import uuid

class FibonacciRpcClient():
    def __init__(self):
        # 创建连接
        credential = pika.PlainCredentials(username='zy',password='123456')
        conn = pika.ConnectionParameters(host='192.168.52.101',credentials=credential)
        self.connection = pika.BlockingConnection(conn)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        # 设置回调
        self.channel.basic_consume(self.on_response,
                                   on_ack=True,
                                   queue=self.callback_queue)
        # self.channel.queue_declare(queue='rpc_queue')

    # def on_reponse(self,ch):
    #     if self.corr_id == props.
    def call(self,n):
        # 设置响应和回调的通道的id
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id),
                                   body=str())

        while self.response is None:
            self.connection.process_data_events()

        return self.response

fib = FibonacciRpcClient()
response = fib.call(20)
print(response)