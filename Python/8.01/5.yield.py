# return和yield的区别
# return 可以往方法外传递一个值,之后return后面的代码统统不再执行
# yield也可以往方法外面传递一个值,但是传递之后,继续回到yield执行
# 通过yield传递值的这个方法是一个可迭代对象
def test(name):
    print('return方法')
    return name
    print('return方法结束')
name = test('张三')
print(name)

def test2(age):
    for i in range(age):
        yield i
        print('hello')
for x in test2(18):
    print('x=',x)