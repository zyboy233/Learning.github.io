
# 创建字典的两种方式
dict1 = {}
dict2 = dict()

# 字典里面所有的值都是以键值对的形式出现的
dict1 = {
    'name':'张三',
    'age':17,
    'friend':['李四','王五','赵六','冯七']
}
# 获取指定key值对应的name值
print(dict1['name'])

# KeyError: 'fond'
# key错误 没有指定的键值'fond'
# print(dict1['fond'])

# 给字典中指定的键 赋值
# 如果有这个键 则修改这个键对应的值
# 如果没有 就创建这个键 并赋值
dict1['fond'] = '学习'
print(dict1)

# dict1.pop()
# pop里面需要写参数,需要删除的key
dict1.pop('friend')
# TypeError: pop expected at least 1 arguments, got 0
# arguments 参数  expected 期望 at least 至少
# 类型错误:pop方法希望得到至少一个参数 但现在参数为0
print(dict1)

# 输出所有的值
print(dict1.values())
print(dict1.keys())

if 'name' in dict1.keys():
    print('存在')
else:
    print('不存在')
if '张三' in dict1.values():
    print('存在')
else:
    print('不存在')

# 获取所有的key和value
for key in dict1.keys():
    value = dict1[key]
    print(key,value)
for key,value in dict1.items():
    print(key,value)

info = {
    'name':'张三',
    'friend_list':[
        {
            'name':'王五',
            'friend_list':[
                '赵六','冯七'
            ]
        }
    ]
}

# for value in info.values():
#     if type(value)

for key,value in info.items():
    if key == 'name':
        print(value)
    else:
        print(value[0]['name'])
        print(value[0]['friend_list'])
