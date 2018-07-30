
def outSide(a,b):
    def inSide():
        return a + b
    return inSide
print(outSide(10,11))
result = outSide(10,11)
print(result)
# 外层函数包含内层函数同时内层函数使用外层函数的参数并
# 且将内层函数返回出去这种现象称为闭包,这种结构称为闭包
# 1.函数包裹函数
# 2.内层函数使用外层函数的参数
# 3.内层函数当成返回值