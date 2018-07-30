
# 会变的量  x,y
# 计算机当中的变量 可以表示任意东西
#字符串 数字 真假 列表 字典 元组 集合 对象 方法

# 注释 起到解释说明的作用  是给程序员看的
# 注释并不会编译和执行

# string int float double char long short bool
# = 赋值
#Python里面没有基本数字类型 那么怎么知道变量是什么类型的变量呢
#答:就看变量后面跟的是什么类型的值
#声明一个变量 并且将a的这个赋给它
a = 1
a = a+1
#b字符串类型
b = '1'
b = "1"
b = '''1'''
b = """1"""
b = "'1'"
b = '"1"'
#布尔类型 bool
c = True

#变量的命名:最好做到见名知意
age = 1
name = '张三'

#bool只有两个值 真假
isReally = False

# 驼峰命名法
# 大驼峰:每一个单词首字母大写
# 小驼峰:首字母小写,其余单词首字母大写

# 下划线命名法
# 每一个单词之间以_相连

MyName = '张三'
myName = '张三'
my_name = '张三'

# 变量名字可以包含数字字母下划线

# python保留字
# 保留字即关键字,保留字即关键字，我们不能把它们用作任何标识符名称。
# Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
import keyword
print(keyword.kwlist)
# >>>['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue',
#     'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
#     'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
#     'return', 'try', 'while', 'with', 'yield']
