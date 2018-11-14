import socket
import hmac
import hashlib
import os

# 自己定义一串密钥
secret_key = b'zyboy'

def conn_auth(conn):
    """认证客户端连接
    :param conn: 客户端的连接
    :return : True/False
    """
    print('开始验证新的连接的合法性!')
    # 随机生成一个32的字符串
    msg = os.urandom(32)
    conn.sendall(msg)
    # h = hmac.new(secret_key,msg)
    h = hmac.new(secret_key,msg,hashlib.sha1)
    digest = h.digest()
    # 获取到客户端返回回来的摘要进行比对
    response = conn.recv(len(digest))
    return hmac.compare_digest(response,digest)
def data_handle(conn,bufsize=1024):
    if not conn_auth(conn):
        print('连接不合法!')
        conn.close()
    else:
        print('连接合法,开始通信')
    while True:
        data = conn.recv(bufsize)
        print(data.decode('utf-8'))
def server_handle(ip_port,bufsize):
    sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    sock.bind(ip_port)
    sock.listen()

    while True:
        conn,addr = sock.accept()
        print('新的连接: {}:{}'.format(addr[0],addr[1]))
        data_handle(conn,bufsize)

if __name__ == '__main__':
    ip_port = ('127.0.0.1',9090)
    bufsize = 1024
    server_handle(ip_port,bufsize)