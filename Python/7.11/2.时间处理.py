
import time
# time.struct_time  结构体
time1 = time.localtime()
print(time)

# 从1970年到现在的秒数
time2 = time.time()
print(time2)

# 从1970年开始往后指定的秒数
time3 = time.localtime(1531274000)
print(time3)

result = time.strftime('%y %m %d %H %M %S',time.localtime())
print(result)
# 线程休眠
#     爬虫:获取对方数据太快,有可能被认为是爬虫程序,所以有时需要减缓速度
#     线程:a代码块的执行受B,必须确保B代码限制性并返回数据,这时候就可以让A代码
#         休眠一段时间(休眠不是必须的,也不是最好的)
#     定时任务:需要代码到指定时间, 去执行某个任务,放时间还未到达,可以让程序先休眠
# time.sleep(1)
print('今天是周三,一星期马上过去有一半了')

import datetime

# 获取现在的日期和时间
date1 = datetime.datetime.now()
print(date1)

date2 = date1.strftime('%y/%m/%d %H:%M:%S')
print(date2)
date2 = date1.strftime('%y year %m month %d day ')
print(date2)

# UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 3: Illegal byte sequence
# '\u5e74' in position 3: Illegal byte sequence
# 编码错误:本地文件不能对指定位置的字符进行编码
# date2 = date1.strftime('%y年%m月%d日')
date2 = date2.replace('year','年').replace('month','月').replace('day','日')
print(date2)

# 怎么获取今天往后推一天时间
# 可以用来计算过期时间
date4 = datetime.timedelta(days= 1 ,hours=12)
date5 = datetime.datetime.now() + date4
print(date5)

# TypeError: Required argument 'year' (pos 1) not found
# date6 = datetime.date()
date6 = datetime.datetime.now()
date7 = date6.date()
print(date7)
print(date7.year,date7.month,date7.day)

date8 = date6.time()
print(date8)

date9 = datetime.datetime.now()
# stamp 邮戳
# timestamp 时间戳 时间线
print(date9.timestamp())