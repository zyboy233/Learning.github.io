import socket

skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
skt.bind(('127.0.0.1',9090))

skt.listen()

while True:
    conn,(ip,port) = skt.accept()
    conn.send('hello'.encode('utf-8'))
    data1 = conn.recv(1024).decode('utf-8')
    print(data1)
    send_msg = b'hello,I am is client! I"m coming'
    send_msg_length = len(send_msg)
    conn.send(str(send_msg_length).encode('utf-8'))
    data_recv = conn.recv(1024).decode('utf-8')
    if data_recv == 'recv_ready':
        conn.send(send_msg)
conn.close()