
# 类: 抽象 整体 全局 人类 星球
# 对象:具体 个体 局部 张三丰 地球
# 对象是从类中分离出来的个体
# 面向对象编程
# object 任何一个对象都直接或者间接继承自object
# java
# oc
# 从功能上定义:类是属性和方法的集合

class Hero(object):
    # 属性  称之为类属性
    blood = 700
    attact = 67
    level = 1
    # 方法
    def skill(self):
        print('致盲设计')
timo = Hero()
timo.skill()

print(Hero.blood)

class People(object):
    # init 初始化
    # 当对象创建的时候 属性的默认值
    # 魔术方法
    count = 0
    # 对象创建的时候会自动调用init方法
    # 如果init方法需要参数的话
    # 那么对象在创建的时候也需要参数
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    # 对象方法
    def sleep(self):
        print('{}一天要睡十七八个小时'.format(self.name))
    def work(self):
        print('{}工作时间太短,不开心'.format(self.name))
    def fond(self):
        print('人生苦短,幸亏我甜')
# 模子------------
zhangSan = People('张三','男',18)
zhangSan.sleep()

print(People.count)
# 类属性可以通过对象调用
print(zhangSan.count)

# AttributeError: type object 'People' has no attribute 'name'
# 属性错误:People没有属性name
# print(People.name)

zhangSan.work()
# TypeError: work() missing 1 required positional argument: 'self'
# 类型错误:work 里面需要用到一个参数self
# work方法是People里面的对象方法 self指的是People的对象
# 所以在调用的时候  需要传入一个People的对象
People.work(zhangSan)

class Person(object):
    # 如果在初始化的时候 设置了默认值
    # 那么在创建对象的时候 可以不必设置参数

    def __init__(self,name='',age='',sex = '',fond = ''):
        self.name = name
        # 属性前面添加下划线的这种方式叫做私有属性
        # 也就是这种属性不想别别人访问的属性
        # 但是这种属性不是绝对访问不了
        # 可以通过添加下划线访问
        self._age = age
        self._sex =sex
        # 属性如果是双下划线 如果想要调用属性
        # 需要通过 p1._Person__fond这种方式调用
        self.__fond = fond
        # get set 方法
        # property  属性
        # attribute 属性
        # argument 参数

        # 声明get set 方法的标记
    @property
    def fond(self):
        print('get方法被调用了')
        return self.__fond
    @fond.setter
    def fond(self,fond):
        print('set方法被调用了')
        self.__fond = fond
p1 = Person('张三丰',149,'男','练剑')
print(p1.name)
print(p1._age)
# AttributeError: 'Person' object has no attribute '__fond'
# 属性错误:Person里面没有这种属性
print(p1._Person__fond)

print(p1.fond)
p1.fond = '练拳'
print(p1.fond)

# def test():
#     pass
# test()