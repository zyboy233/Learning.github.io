
def test():
    pass
test()

def test(a):
    pass
test('a')

a = 0
def test():
    global a
    a = 'xx'
test()
print(a)
# print(b)

def test():
    return 1
print(test())

def test(a):
    return a+1
print(test(1))

def test(a,b=3):
    print(a+b)
test(3)

# 默认参数放队尾
# 普通形参必须放在默认参数前面
# def test(b= 3,a):
#     pass
# test()

def testA():
    return
def testB(argument):
    print(argument)
# 函数里面的参数可以为任意类型
testB(testA())

def test(a,*args):
    print(a)
    print(args)
test(1,2,3,4,5,6)
