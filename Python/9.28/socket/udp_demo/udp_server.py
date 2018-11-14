import socket

# 1. 初始化socket
udp_skt = socket.socket(type=socket.SOCK_DGRAM)

# 2. 绑定本地ip和端口
udp_skt.bind(('127.0.0.1',9001))

# 3. 接收/发送消息
client_msg,client_addr = udp_skt.recvfrom(1024)
print('收到了客户端的数据:',client_msg.decode())

# 发送消息
print(client_addr,'========')
udp_skt.sendto('我是udp的服务端'.encode(),client_addr)

# 4. 关闭
udp_skt.close()