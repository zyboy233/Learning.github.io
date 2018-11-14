import socket

skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

skt.connect(('127.0.0.1',9090))

# b("hello") 表示byte类型
# 因为流的传输形式为byte类型,所以把字符串转为byte类型
# skt.send(b'helloo')

# 循环发送和接收数据
while True:
    # skt.send(b'')
    server_msg = skt.recv(1024).decode('utf-8')
    print(server_msg)
    skt.send('hello1'.encode('utf-8'))
    length = int(skt.recv(1024).decode('utf-8'))
    skt.send('recv_ready'.encode('utf-8'))
    server_msg = skt.recv(length)
    print(server_msg.decode('utf-8'))
skt.close()