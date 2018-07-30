
# for 循环是迭代/遍历的重要形式
# range 范围
# range(10) 从0到9
# randint(0,10)  从0到10
for index in range(10):
    print(index)
# enumerate 枚举
for index in enumerate(range(100,110)):
    print(index[1])
for x,y in enumerate(range(100,110)):
    print(y)
for index in range(100,200,10):
    print(index)
