
# python 里面容器的种类有几种
# list
# tuple
# set
# dict
# list里面的元素是可变的 可以进行增删改查
# tuple里面的元素是可变的 只能查看 不饿能增删改



tp1 = ()
tp2 = tuple()

tp1 = ((),[],{},1,2,3,'a','b','c',3.14,True)
print(tp1[:])
print(tp1[1::2])
print(tp1[5])
# AttributeError: 'tuple' object has no attribute 'remove'
# attribute 属性 object 对象
# 属性错误
# tp1.remove(1)
print(tp1)

# 作业4:重现8种错误