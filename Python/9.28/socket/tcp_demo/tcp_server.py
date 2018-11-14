import socket

# 1. 创建socket对象
# sock_stream tcp
# sock_dgram udp
skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# 2. 绑定本地ip和端口
skt.bind(('127.0.0.1',9000))
# 3. 监听
skt.listen()

# 4. 接收消息 (客户端发来的请求,没有就一直阻塞)
print("Accept start...")
client_skt,client_addr = skt.accept()
print(client_skt,'===',client_addr)

# 5. 接收/发送消息
recv = client_skt.recv(1024)
print(recv.decode())
# 发送给client
client_skt.send('我收到了你的消息'.encode())

# 6. 关闭
client_skt.close()
skt.close()