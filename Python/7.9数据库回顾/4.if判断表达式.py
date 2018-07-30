
# if 如果
# if后面会跟一个判断条件  这个条件只会为真假
# =赋值 将=右边的值赋予=左边的变量
# ==逻辑等  表示判断 判断左右两边的变量是否一致
name = '小王'
# 使变量与值进行判断     尤达表达式
# 而不用值和变量来判断
if name == '小王':
    # pass作用当没有什么代码可写的时候
    # 而程序又要你一定写代码 否则报错
    # 那么这个时候就可以写pass
    # 表示此处是有代码的 是程序不会报错
    # 但是不会产生实际影响
    # pass
    print('来人正是小王')

# if elsez这种结构是二选一的
# 只有一个条件会被执行
# 而且必有一个条件会被执行
if name == '小王':
    print('来人正是小王')
else:
    print('来者何人')

# if elif else 这种结构
# 前面的判断条件只有一个能够成立被执行
# 其他的都不会被执行
# 如果所有的判断都不成立
# 就会执行else里的条件
score = 60
if score >= 90:
    print('优秀')
# elif 后面必跟判断条件
elif score >= 80:
    print('良好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
# else 后面无需写判断条件
else:
    print('不及格')

# 所有条件为互斥条件  只有一个能够满足
# 如果多个条件同时能满足
# 则执行第一个满足的条件
money = 100
if money < 100:
    print('少于100')
elif money < 200:
    print('少于200')
elif money < 500:
    print('少于500')
elif money < 1000:
    print('少于1000')
else:
    print('土豪')

count = 100
# if和if之间没有任何关系
# 上一个if是否执行
# 并布影响下一个if的执行
# 注意:每一个if就是一个新的判断条件的开始
if count < 50:
    print('总数少于50')
if count < 100:
    print('少于100')
if count < 200:
    print('少于200')
if count < 500:
    print('少于500')
