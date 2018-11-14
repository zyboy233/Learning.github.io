import socket

skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

skt.bind(('127.0.0.1',8001))

skt.listen()

client_skt,client_addr = skt.accept()

# client_skt.send(b'HTTP/1.1 200 OK\r\r\n')
# client_skt.send('哈哈哈'.encode())

# 循环的续写操作
while True:
    client_msg = client_skt.recv(1024)
    if client_msg.decode() == '你好':
        print('client:',client_msg.decode())
    server_msg = client_msg
    client_skt.send(server_msg)

client_skt.close()
