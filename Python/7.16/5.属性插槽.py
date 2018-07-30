
name = '小明'
age = 6
print('{},{}'.format(name,age))
print('{},{}'.format(age,name))

class People(object):
    def __init__(self,name='',age=''):
        self.name = name
        self.age = age
p = People('赵云',27)
print(p.name)
print(p.age)

# 给对象添加一个属性
p.fond = '学习'
print(p.fond)
dic = {}
# 无则添加 有则修改
dic['name'] = '小兰'
print(dic['name'])

class Person(object):
    # slots 插槽
    # 只支持本类添加[]列表里面包含的属性
    __slots__=['name','age']
    def __init__(self,name='',age = ''):
        self.name=name
        self.age = age
p1 = Person('杨戬',500)
print(p1.name)
print(p1.age)

# p1.dog = '哮天犬'
# print(p1.dog)
