
# 创建列表的两种方式
list = []
# list2 = list()

# 每两个元素之间以逗号2隔开
list = ['hello world',[[]],1,3.14,True]

list1 = ['outMan','小李子','诺兰','皮克斯']

#获取列表里面索引为0的这个元素
print(list1[0])
# IndexError: list index out of range
# 索引错误:列表索引超出范围
# print(list[5])
# 如果:左右两边都不写值,表示获取所有的元素
print(list[:])
# :左边表示从指定索引开始
# :右边表示到指定索引结束(不包含该位置)
print(list[1:1])
# 值1:开始的位置
# 值2:结束的位置
# 值3:隔几个元素
print(list1[1::2])
# 倒叙
print(list1[::-1])
# 正序
print(list1[::-1])

# -------------------------------insert------------------------------

list1 = [1,2,3,4,5,6,7]
# insert 会指定插入的位置

# list1.insert(2,'hello')
print(list1)
# 追加的内容  默认放在列表的队尾
list1.append('World')
print(list1)
list1.extend('张三')
print(list1)

list1 = [1,2,3]
list2 = ['a','b','c']
# append 追加内容
# 不管追加的是什么类型的内容
# 都会将这块内容当作一个整体
# 放入到被添加的列表中
# list1.append(list2)
print(list1)
# extend 扩展
# 将扩展对象的每一个元素
# 分别添加到被扩展对象之中
list1.extend(list2)
print(list1)

list1 = [1,2,3,4,3,2,1]
# pop 将最后一个元素弹出
list1.pop()
print(list1)

list1.pop(2)
print(list1)
# 删除所有符合指定要求的这些元素中索引最小的一个
list1.remove(2)
print(list1)
list1 = ['a','b','c','d']
# 查看列表当中有没有指定的元素
if 'b' in list1:
    print('存在')
else:
    print('不存在')

list1 = ['a','b','c','d']
# reverse 相反的
list1.reverse()
print(list1)
# 获取列表里面指定元素的索引
result = list1.index('a')
print(result)

# 作业3:代码实现extend,将任意容器里的元素放入到另外一个容器当中

list1 = [3,6,1,9,2,7,5]
list1.sort()
list1.reverse()
print(list1)
