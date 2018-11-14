"""
1.ISO七层模型

2. 常用协议

http smtp pop3 ftp :应用层

http:超文本传输协议
ftp: 文件传输协议

ssl: 在会话层
ssl: 安全套接字层协议

tcp upd : 传输层
tcp : 传输控制协议
udp: 用户报文协议

3. 端口 port 总端口数 2^16-1 =65535
http 80
https 443
mysql 3306
django 8000
ssh 22

0-1024 知名端口,勿随便占用
netstat -lnp | grep <port> 查看端口号占用情况

4. ip地址
    IPv4  IPv6

    DNS DomainNameSystem 域名解析系统
    8.8.8.8 google提供
    114.114.114.114 国内

    一个域名可以对应多个ip
    www.baidu.com 一级域名
    image.baidu.com 二级域名
    image.upload.baidu.com 三级域名

    ip地址ABCDE五类

5. Socket
    1) 是套接字,用于描述ip地址和端口
    2) 是一种通信机制
    3) 位于传输层与应用层之间,是一个抽象层
    
"""