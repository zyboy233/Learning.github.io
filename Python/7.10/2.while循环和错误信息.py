
# while后面的判断条件如果为真
# 那么里面的代码块会一直执行
# 直到程序结束或者跳出循环或者条件为假
# while True:
#     pass

age = 1
while age < 18:
    print('未成年{}'.format(age))
    age += 1

count = 0
while True:
    count +=1
    if count >=10000:
        # break   打断
        # 当循环里面执行了break
        # 那么后面的循环都不再执行
        break
    print(count)
    # break 跳出循环,循环外面的代码继续执行
    # continue 跳出这一次循环,剩下的循环继续执行
    # return 通常用在方法中 后面的代码统统不执行
count = 0
while count < 10:
    count += 1
    if count == 4:
        continue
    print('count为{}'.format(count))

# return 不能在方法以外执行
# SyntaxError: 'return' outside function
# 解决:将return放进方法体中

# while True:
#     count += 1
#     if count ==20:
#         return

# IndentationError: expected an indented block
# 解决:缩进
# if count == 0:
# print(count)
# else:
#   print('nothing')

# for 后面的循环次数/范围了,注重自己来控制循环的次数
# while 后面写判断的条件,注重条件的真假
