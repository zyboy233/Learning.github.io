
# str = ''
# str =""
# str =''''''
# str =""""""
"""
Python里面的多行注释用这种方式
其实质 就是一个大字符串
"""
# 字符串:一串字符连接在一起,称之为字符串
# 字符:
# 在有基本数据类型的其他语言里面:char声明的是字符串 string声明的字符串
# char
# string
# 在引号里面写的内容 不管是什么  都是一个字符串
content = ''
content = 'Hello world'
# ------------------------------字符串切片操作------------------------
# 字符串也是一个容器 可以存放任意字符
# 容器里面所有的元素都有一个编号
# 编号从0开始
print(content[0])
# IndexError: string index out of range
# 索引错误:字符串超出了范围
# 解决办法:查看字符串的长度  索引要小于长度
# 写一篇博客 记录所有的错误信息
# print(content[21])
# 获取指定索引开始到结束的字符串内容(包含指定索引的这个开始位置)
print(content[3:])
# 获取字符串开始到指定索引的内容(不包含制定索引的这个位置)
print(content[:3])
# hello world
print(content[3:6])
# :前面是开始位置 如果不写 默认是0
# :后面是结束位置 如果不写 默认到结尾
print(content[:-1])
# hello world
print(content[1:-1])
# 倒序
print(content[::-1])
# hello world
# 值1:开始位置
# 值2:结束位置
# 值3:每次往后隔几位,默认是1
# 对比函数  range(1,5,2)
print(content[1::2])

# 以上操作都没有真正改变原来字符串内容
# 如果要改变  需要这样写
content = content[1:4]
print(content)
# ---------------------------find--------------------------
content = 'Hello World'
# 查看content里面有没有指定的字符串
# 如果返回-1 则表示没有找到指定的内容
# 若果返回其他值 表示找到 返回的值为该字符在字符串当中的索引
result = content.find('l')
print(result)
# 晚自习作业2:不能使用find方法,自己模拟find方法的实现过程
#     判断字符串当中有没有包含指定字符,如果有,返回其在字符串
#     中的位置,若果没有 返回-1

# -------------------------------index-------------------
content = 'Hello World'
# ValueError: substring not found
# 值错误:子字符串未找到
result = content.index('r')
print(result)

# ---------------------------count-----------------------
content = 'Hello World'
# 获取指定字符在字符串当中的个数
result = content.count('o')
print(result)

# ------------------------replace--------------------------
content = 'hello world'
result = content.replace('l','t')
print(result)

# --------------------------split------------------------------
content = 'hello world'
result = content.split('l')
print(result)

# ----------------------------大小写转化---------------------
content = 'hello WORLD'
# 字符全部小写  只能转化英文字母的大小写
print(content.lower())
# 字母全部大写
print(content.upper())
# 首字母大写 其余小写
print(content.capitalize())
# 转化成小写 支持utf-8
print(content.casefold())

# ---------------------------start,end--------------------------
content = 'Hello World'
# start ,end 会返回一个bool
print(content.startswith('w'))
print(content.endswith('d'))

# ----------------------------maketrans----------------------
content = '习近平近日来智游某基地进行参观并作出了重要讲话'
# 制作规则:将智游替换成XX
s = str.maketrans('智游','XX')
# 让content 遵守这个规则
content  = content.translate(s)
print(content)
# 类似
        # re = content.replace('习近平','XX')
        # print(re)
