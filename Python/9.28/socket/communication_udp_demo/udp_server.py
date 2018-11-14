import socket

udp_skt = socket.socket(type=socket.SOCK_DGRAM)
udp_skt.bind(('127.0.0.1',9002))

while True:
    client_msg,client_addr = udp_skt.recvfrom(1024)
    print('来自[{}:{}]的消息:{}'.format(client_addr[0],client_addr[1],client_msg.decode()))
    back_msg = input('回复消息:')
    udp_skt.sendto(back_msg.encode(),client_addr)