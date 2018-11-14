import socket

tcp_skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

tcp_skt.connect(('127.0.0.1',8001))

while True:
    client_msg = input(">>>>>>:")
    tcp_skt.send(client_msg.encode())
    server_msg = tcp_skt.recv(10240)
    print(server_msg.decode('GBK'))