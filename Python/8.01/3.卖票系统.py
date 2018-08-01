import threading
import time
import random
class buyer(object):
    def __init__(self,name = '',number=1):
        self.number = number
        self.name = name
lock = threading.Lock()
class computer(object):
    def __init__(self,count = 0):
        self.count = count
    def qurey_with_buyer_info(self,other):
        lock.acquire()
        print('正在为{}查询剩余票数'.format(other.name))
        time.sleep(random.randint(1,3))
        if self.count > other.number:
            print('有票,{}可以购买'.format(other.name))
            time.sleep(random.randint(1,3))
            self.count -= other.number
        else:
            print('没票')
        lock.release()

hanmeimei = buyer('韩梅梅',2)
houzi = buyer('猴子',5)
com = computer(6)

thread1 = threading.Thread(target=com.qurey_with_buyer_info,name='thread1',args=(hanmeimei,))
thread2 = threading.Thread(target=com.qurey_with_buyer_info,name='thread2',args=(houzi,))

thread1.start()
thread2.start()