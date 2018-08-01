# 进程和线程的区别:
# 1.进程: 每个程序都会有一个进程,负责管理程序各个功能的执行,进程只会有一个
#     而且至少有一个(相当于包工头)
# 2.线程: 每个进程里面至少有一个线程,称之为主线程,除此以外还会有其他线程,称之为分线程
#     线程是控制任务执行的最小单位(相当于农民工)
# 3.进程负责控制各个线程的执行,当程序运行,进程启动,程序关闭,进咸亨结束

# 主线程和分线程:
# 1.代码运行默认在主线程里面.如果执行新的任务,可以开辟分线程
# 2.分线程个数没有限制,分线程里面的任务结束后,分线程结束
#
# 分线程的使用场景:
# 1.当有大量任务需要执行的时候,可以将任务放到分线程里面
# 2.当有大量任务需要执行的时候,而任务的执行顺序需要指定的时候,可以使用分线程
# 3.当界面有大量界面需要更新的时候,放入分线程

# 同步任务: 上一个任务没有完成,下一个任务不能开启
# 异步任务: 同时执行多任务
# 分线程和异步的区别:
# 1.分线程可以同时执行多个任务,所有任务分线程自己完成
# 2.异步可以同时开启多个任务,但是自己只做一个任务,其他任务命令其他人执行

# python里面有两个负责线程的模块,thread,threading
# threading在thread模块基础之上做出扩展
# thread 线程
import threading
import time

# 获取当前线程的名称
print('当前线程为:',threading.current_thread().name)

def myThread():
    print('位置1',threading.current_thread().name)
    print('位置2',threading.current_thread().name)
    print('位置3',threading.current_thread().name)
    print('位置4',threading.current_thread().name)
    print('位置5',threading.current_thread().name)
    print('位置6',threading.current_thread().name)

# class People(object):
#     def thread_test(self):
#         print('对象方法',threading.current_thread().name)
# p = People()
# p.thread_test()

# threading.Thread开辟一个新线程  target 目标
sub_thread = threading.Thread(target= myThread,name='newThread')
sub_thread.start()

# 确保任务的执行顺序 自己线程先完成,之后执行其他线程
sub_thread.join()
# 当程序运行时 会先在主线程中执行(因为在程序刚开始时
# 只有主线程,没有分线程)
# 然后会根据情况进入到分线程,主线程和分线程的任务时交叉运行的
# 自己线程的执行情况不会影响对方线程
# 分线程代码结束以后,回归到主线程
print('outthread1',threading.current_thread().name)
print('outthread2',threading.current_thread().name)
print('outthread3',threading.current_thread().name)
print('outthread4',threading.current_thread().name)
print('outthread5',threading.current_thread().name)
