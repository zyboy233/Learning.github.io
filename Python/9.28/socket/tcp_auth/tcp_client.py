import socket
import hmac
import hashlib

secret_key = b'zyboy'

def conn_auth(conn):
    """
    认证客户端连接
    :param conn:
    :return:
    """
    msg = conn.recv(32)
    # h = hmac.new(secret_key,msg)
    h = hmac.new(secret_key,msg,hashlib.sha1)
    digest = h.digest()
    conn.sendall(digest)

def client_handle(ip_port,bufsize=1024):
    """
    :param ip_port:
    :param bufsize:
    :return:
    """
    sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    sock.connect(ip_port)
    conn_auth(sock)

    while True:
        data = input('请输入要给服务器的数据: ')
        sock.sendall(data.encode('utf-8'))
    sock.close()

if __name__ == '__main__':
    ip_port = ('127.0.0.1',9090)
    bufsize = 1024
    client_handle(ip_port,bufsize)