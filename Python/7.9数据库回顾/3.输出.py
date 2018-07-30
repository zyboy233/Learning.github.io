
# 运行代码的方式有三种
# 1.右键 run
# 2.右上角绿色小三角
# 3.shift + F10(确保用之前两种方式运行过)

name = '今天是七月九日,星期一,Python9期正式上课第一天'

# print为输出 是python里面非常重要的调试工具
# print输出默认是换行的,若不换行在后加end="",如:
print(name,end="")

name = '你好'
print(name)

name = '张三'
age = 16
# 字符串拼接
# TypeError: must be str, not int
# 使用+进行字符串拼接的话,变量类型只能是字符串  不能为其他类型
print('我叫做' + name + ',我今年' + str(age) + '岁了')

des = '漂亮的'
count = 2
# %s 占位符 先占一个位置 然后往对应的位置上添加内容
print('墙上挂了%s副%s的画' % (count, des))

name = '小张'
age = 23
# format 格式
print('有一个朋友{},今年已经{}岁了'.format(name,age))


