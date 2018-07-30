# beautiful 美丽的,漂亮的
# soup 汤
# beautifulsoup是一个python的第三方库
# 和xpath作用一样 都是用来解析html数据
# 相比之下 xpath速度更快
# xpath底层用c实现

from bs4 import BeautifulSoup

# beautifulsoup里面需要两个参数
# 一个为open方法 一个为固定写法'lxml'
# open方法里面需要两个参数
# 1.想要解析的数据
# 2.设置编码格式
bs = BeautifulSoup(open('index.html',encoding = 'utf-8'),'lxml')
print(bs)
print(type(bs))

# 获取网页当中的title标签
print(bs.title)
# 获取head标签及head标签内部的其他标签
print(bs.head)
# 获取网页当中的第一个a标签
print(bs.a)
# 总结:bs.xx
# 获取所有xx当中的第一个xx以及第一个xx里面的内容
# document 文档
# 获取当前内容的标签名 bs为一个整体 而不是某一个具体的标签
print(bs.name)
# 获取head的标签名
print(bs.head.name)
# 获取title的标签名
print(bs.title.name)
# attr
# attribute 属性
# 获取指定标签的所有属性
# 如果没有做特别处理,bs.xx永远获取的是所有xx中第一个xx
print(bs.div.attrs)
# keyError只能从自己有的属性当中找
print(bs.a['id'])
print(bs.a['href'])
# class和id不一样
# id必须是唯一的 一个标签只能有一个id
# class不是唯一的 不同的标签可以拥有用一个class
# 同一个标签一可以拥有多个class
print(bs.a['class'])
print(bs.html['lang'])

# delete 删除
print(bs.a)
del bs.a['id']
print(bs.a)
# 获取指定标签的文本内容
print(bs.a.string)
# string获取的文本指的是本标签的文本
# 不包含子标签的文本
print(bs.div.string)
# 遍历--------------------
# contents能够获取指定标签下的所有内容
print(bs.head.contents)
print(bs.body.contents)
# 获取所有内容当中指定索引的内容
print(bs.div.contents[3])
# parent 父级
# 获取指定标签的父级标签和父标签内部的所有内容
head = bs.title.parent
print(head)
# tag 标签
print(type(head))

re = bs.find_all('a')
print(re)
for value in re:
    print(value)
# id是唯一的 通过id来找 只能找到一个 所以用find
# class不是唯一的 通过class来找 可能找到多个
print(bs.find(id="jd"))
print(bs.find_all(class_='shopping'))
# 找到所有符合条件的第一个
print(bs.find(class_='shopping'))
print(bs.find_all(id='jd'))

# select--------------------------选择
print(bs.select('title'))
# 当选择的对象有多个的时候 就获取所有的对象
print(bs.select('a'))
# .表示类名 #表示id
print(bs.select('.first'))
print(bs.select('#jd'))
# print(bs.select('href'))
# 找到一个类名为now的div标签
print(bs.select('div.now'))

