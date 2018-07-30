
# import os
# current_path1 =  os.getcwd()
# current_path2 = os.path.abspath('.')
#

# list1 = [1,65,7,3,88,42]
# list1 = sorted(list1,key = lambda x:x)
# print(list1)

# def testFun(name,sex='男',*args,**kwargs):
#     print(name)
#     print(sex)
#     print(args)
#     print(kwargs)
# testFun('小红','女','18岁','贤惠','漂亮',fond='game',qq=110)

# class A(object):
#     def __init__(self,name='',age=''):
#         self.name = name
#         self.age = age
# class B(A):
#     def __init__(self,name,age):
#         super(B,self).__init__(name,age)
# b = B('张三',100)

# class A(object):
#     @classmethod
#     def test(cls):
#         print('声明类方法调用我')
# A.test()

str1 = 'asfe,efasew,fef'
result  = str1.split(',')
print(result)
print(id(str1))
print(id(str1.split(',')))


# str = 'eafadfe'
# s = str.maketrans('ad','13')
# str = str.translate(s)
# print(str)