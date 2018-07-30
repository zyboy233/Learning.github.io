
# 函数就是方法 非常类似现实生活当中的模板/摸具
# 声明方法 def define 定义 test方法名称 ()内部写参数
def test():
        pass
test()
# 无参数无返回值
def firstFun():
    print('this is my first function')
firstFun()

# 有参数无返回值 声明方法中的参数叫做形式参数 简称形参
    # 形参没有具体的值  本身为一个变量
def secondFun(value):
    print('我喜欢{}'.format(value))
    # 调用方法的时候的参数   叫做实际参数 简称实参
    # 实际不是变量  而是具体的值
secondFun([1,2,3])

# 局部变量 和 全局变量---------------------------------------
list = []
dic = {}
name = 'summer'
age = 0
fond = 12113
def partFun():
    # 在方法内部声明的变量叫做局部变量
    # 只能在方法内部使用
    # 出了这个方法就释放了
    global fond
    fond = '学习'
    print(fond)
    print(name)
partFun()
print(name)
print(fond)

# 无参数有返回值
def thirdFun():
    love = '爱学习'
    return love
result = thirdFun()
print(result)

def fourFun():
    print('Hello')
    # return后面如果没有跟值的话 默认返回None
    # return只能写在方法里面 不能在方法外面使用
    # 代码执行了以后  return到方法结束之前
    # 的部分 统统不执行
    return
    print('World')
fourFun()

# 有参数有返回值
def fiveFun(a,b):
    return a + b
print(fiveFun(12,13))

# 有多参有返回值
def sixFun(a,b,c,d,e,f):
    print(a)
    print(b)
sixFun('a',0,[1,2,3,4,5,6],True,{'name':'张三'},(1,2,3))

# 默认参数
def myGirlFriend(name,age,sex=True,born = '未知'):
    print('我的女朋友是{},年龄是{},性别是{},出生日期是{}'.format(name,age,sex,born))
myGirlFriend('小玲',100)
myGirlFriend('小王',100,True,'1918年')
myGirlFriend('小黄',100,True)

# 关键参数
def myBoyFriend(name,age,sex=False,born='未知'):
    print('我的男朋友是{},年龄是{},性别是{},出生日期是{}'.format(name,age,sex,born))
myBoyFriend('小张',100)
# 指明给哪个参数设置值 这种参数叫做关键参数
myBoyFriend('小张',100,born='2000年1月1日')

# *args参数
# argument 参数
# *args 能将多余的参数 统统放到自己内部
def myArgu(name,*args):
    print(name)
    print(args)
myArgu('张三丰',149,'武当创始人','太极剑','太极拳')
