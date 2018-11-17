"""
[uwsgi]
# 通过uwsgi访问django需要配置成http
# 通过nginx请求uwsgi来访问django 需要配置成socket
# 9000 是django的端口号
socket = 0.0.0.0:9001

# web项目根目录
chdir = /home/admin/wechat/mysite

# module指定项目自带的的wsgi配置文件位置
module = mysite.wsgi

# 允许存在主进程
master = true

# 开启进程数量
processes = 3

# 服务器退出时自动清理环境
vacuum = true
"""