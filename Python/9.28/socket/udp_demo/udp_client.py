import socket

# 1. 初始化
udp_skt = socket.socket(type=socket.SOCK_DGRAM)

# 2. 发送消息
udp_skt.sendto('我是udp的客户端'.encode(),('127.0.0.1',9001))
# 接收服务端的消息
server_msg,address = udp_skt.recvfrom(1024)
print(server_msg.decode())

udp_skt.close()