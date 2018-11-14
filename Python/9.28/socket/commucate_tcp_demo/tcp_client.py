import socket

skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 连接服务端
skt.connect(('127.0.0.1',8001))

while True:
    client_msg = input('client:')
    if client_msg == 'q':
        print('退出!')
        break
    # 客户端向服务端发送消息
    skt.send(client_msg.encode())
    # 从服务端接收消息
    server_msg = skt.recv(1024)
    print('server:',server_msg.decode())

skt.close()