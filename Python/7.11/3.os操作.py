
# os operation system
# mac os
# ios iphone os

import os

# os可以获取本机的基本信息以及可以对文件
# 及文件夹进行相关操作

# nt 代表windows操作吸系统
# posix代表Linux操作系统
name = os.name
print(name)

# 获取cpu核数
cpu_count = os.cpu_count()
print(cpu_count)

# 判断是否存在某个文件
# path 路径 exists 存在
    # 如果不写路径地址 直接写文件名字
    #  那么默认使用的是相对路径
result = os.path.exists('test.txt')
print(result)

# D:\OneDrive\Python\智游\Python第九期\7.11
result = os.path.exists('d:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result)

# D:\OneDrive\Python\智游\Python第九期\7.11
# 获取绝对路径
result = os.getcwd()
print(result)

# abs absolute
result = os.path.abspath('.')
print(result)

# 获取当前路径的父级路径
result = os.path.abspath('..')
print(result)

# 获取整个地址当中的最后一部分
result = os.path.basename('http://www.baidu.com/music/prettyboy.mp3')
print(result)

result = os.path.basename('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result)

# 地址路径会被/分割成几部分
result = os.path.commonpath(['http://www.jd.com',
                             'http://www.taobao.com',
                             'http://www.baidu.com'])
print(result)

# 返回文件所在的文件夹
# 文档:返回一个文件夹的共有路径
result = os.path.dirname('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result)

# 文件夹信息处理--------------------------------------------------
import time
# get 得到 c change / create 创建时间
result = os.path.getctime('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(time.localtime(result))

# a access 访问时间
result = os.path.getatime('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(time.localtime(result))

# modify 修改时间
result = os.path.getatime('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(time.localtime(result))

# 获取文件大小 获取的大小为字节
result = os.path.getsize('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result/1024)

# is 是否
result = os.path.isfile('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result)

# 返回一个元组 由路径和最后的文件名字组成
result = os.path.split('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result)

# splitext
# 返回一个元组 由全部路径和最后的文件后缀组成
result = os.path.splitext('D:/OneDrive/Python/智游/Python第九期/7.11/test.txt')
print(result)

# FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'D:/OneDrive/Python/智游/Python第九期/7.11/test.txt'
# 文件存在错误:
if os.path.exists('python'):
    os.removedirs('python')
    os.mkdir('python')
else:
    os.mkdir('python')
# os.rename('test.txt','发布.txt')

# 文件读写操作-------------------------------------------------
# 值1:写入的文件 如果有这个文件就直接写入 没有就创建
# 值2:对文件操作的方式 w 表示写入 write 写入
# 值3:文件的编码方式 utf - 8防止乱码出现
# f = open('python.txt','w',encoding='utf-8')
# f.write('今天是周三,七月十一日,距离毕业还有120天\n')
# # 当文件关闭以后  不能对文件进行读写
# f.write('明天是周四,后天是周五,发后天是自习,大后天就休息\n')
# f.close()

# 追加
f = open('python.txt','a',encoding='utf-8')
f.write('新来的内容-------------------------\n')
f.close()

f = open('python.txt','r',encoding='utf-8')
# f.readlines将所有的数据放到一个数组当中
# f.read 将所有的数据放到一个字符串当中
result = f.readlines()
print(result)
f.close()





