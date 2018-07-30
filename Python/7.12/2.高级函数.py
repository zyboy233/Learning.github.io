
space = '-----'
code = 'Hello World'
print(space.join(code))

def test(content,insert):
    print(insert.join(content))
test('今天是周四,马上周六,好开心','!')

# map reduce
def newMap(value):
    return value
# map里面需要两个值
# 值1:必须是函数
# 值2:序列/容器
# 作用:将序列里面的每个元素单独放在函数中执行
list(map(newMap,[1,2,3,4]))

# 需求:将数据库表里所有的数据添加一个完成时间
# map的作用就是依次处理序列里的所有元素
# 和for循环非常相似
def changeAllData(value):
    return '完成时间:2018-8-8'+value
result = list(map(changeAllData,['学习ajaxs','学习AFnet','学习FMDB']))
print(result)

from functools import reduce
def newReduce(value1,value2):
    # reduce会将所有的元素操作两次
    # 实现步骤是:
    # 将任意一个值前面的两个值进行处理
    # 处理的结果再和这个值进行处理
    # 处理的结果给下一个值使用
    # 所以必需有返回值
    return value1+value2+':'
result = reduce(newReduce,['小王','小张','小美','小明'])
print(result)

def count(index1,index2):
    return index1 + index2
result = reduce(count,[1,2,3])
print(result)

def test(a,*args,**kwargs):
    print(a)
    print(args)
    # kwargs必须一个关键参数,不能为字典类型
    print(kwargs)
# SyntaxError: positional argument follows keyword argument
# 方法里面的实参必须和形参对应
# test('张三',17,True,'李四',{'name':'王五'},friend = '赵六','hello world')
test('张三',17,True,'李四',{'name':'王五'},friend = '赵六')

# coding:utf-8
content = 'print("hello world")'
print(content)
# 将指定的字符串当作代码处理
eval(content)

# 声明一个函数 可进行任意的加减乘除运算
def myFun(content1,method = '+'):
    content1 = method.join(content1)
    print(eval(content1))
myFun('123456','/')

# 匿名函数
# 函数都是有名字的 没有名字的函数叫做匿名函数
# lambda表示该函数为匿名函数 匿名函数后面的x表示接受的参数
# :x 表示返回x
result = lambda x : x
print(result(2))

result = lambda x,y : x+y
print(result(3,4))

def test(x,y):
    return x+y
print(test(3,4))

list = [15,78,24,68,99]
# sorted 排序  reverse = True 反序
list = sorted(list,key = lambda x:x,reverse = True)
print(list)

list = [
    {'name':'张三','age':20,'high':178},
    {'name':'李四','age':18,'high':180},
    {'name':'王五','age':22,'high':174}
]
list = sorted(list,key = lambda x:x['high'])
print(list)

