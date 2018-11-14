import socket
import subprocess

tcp_skt = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
# tcp_skt.setsockopt()

tcp_skt.bind(('127.0.0.1',8001))

tcp_skt.listen()

while True:
    client_skt,client_addr = tcp_skt.accept()
    print('客户端:',client_addr)
    while True:
        cmd = client_skt.recv(1024)
        res = subprocess.Popen(cmd.decode(),shell=True,stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        # 标准输出错误
        stderr = res.stderr.read()
        # 标准输出结果
        stdout = res.stdout.read()
        client_skt.send(stderr)
        client_skt.send(stdout)
