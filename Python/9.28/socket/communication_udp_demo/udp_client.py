import socket

udp_skt = socket.socket(type=socket.SOCK_DGRAM)

name_dict = {
    "egg":('127.0.0.1',9002),
    "zhangsan":('127.0.0.1',9002),
    "lisi":('127.0.0.1',9002),
    "wangwu":('127.0.0.1',9002)
}
while True:
    client_name = input('请输入聊天对象:')
    if client_name == 'q':
        print('已退出聊天')
        break
    address = name_dict.get(client_name,('127.0.0.1',9002))
    udp_skt.sendto((client_name +'--'+ input('{}:'.format(client_name))).encode(),address)
    server_msg,server_address = udp_skt.recvfrom(1024)
    print('server:',server_msg.decode())
udp_skt.close()