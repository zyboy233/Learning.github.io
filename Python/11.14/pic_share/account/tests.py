from django.test import TestCase

# Create your tests here.

import random

alist = [1,2,3,4,5,6,7]

random.shuffle(alist)
print(alist)

import os,sys

print(os.path)
print(sys.path)

from urllib import parse
str1 = "name=张三"
# 编码
str2 = parse.quote(str1)
print(str2)
# 解码
str3 = parse.unquote(str2)
print(str3)

import datetime
def dayofyear():
    # year = input("请输入年份：")
    year = '2018'
    # month = input("请输入月份：")
    month = '11'
    # day = input("请输入天：")
    day = '14'
    date1=datetime.date(year=int(year),month=int(month),day=int(day))
    print(date1)
    date2=datetime.date(year=int(year),month=1,day=1)
    print(type(date2))
    return (date1 -date2).days

print(dayofyear())

adict = {key:value for (key,value) in {'a':1,'b':2}.items()}
print(adict)
alist = [a for a in [1,2,3]]
print(alist)

def iterable(a):
    while a < 10:
        yield a
        a+=1
agen = [a for a in iterable(5)]
print(agen)

seq = [1,2,3]
print(id(seq))
print(id(seq[:]))