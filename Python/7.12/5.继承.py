
# object 祖类或者超类
# 子类能继承父类的属性和方法
# class People():
#     pass
#     def __init__(self,name = '',sex = '',fond = ''):
#         self.name = name
#         self.sex = sex
#         self.fond = fond
#     def eat(self):
#         print('活着的目的是为了吃')
# class Man(People):
#     def __init__(self,name,sex,fond,huZi = ''):
#         # 继承父类的属性
#         super(Man,self).__init__(name,sex,fond)
#         self.huZi = huZi
#     def eat(self):
#         super(Man, self).eat()
#         # 重写父类的同名方法
#         print('我张三丰饿死也不吃你们一口饭')
# sanfeng = Man('张三丰')
# sanfeng.name = '三丰'
# print(sanfeng.name)
#
# sanfeng.eat()



