import socket

# 1. 初始化socket
skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

# 2. 连接服务端
skt.connect(('127.0.0.1',9000))

# 3. 发送消息
skt.send('我是你大爷,tcp的client.'.encode())
# 接收server消息
recv = skt.recv(1024)
print(recv.decode())

# 4. 关闭socket连接
skt.close()