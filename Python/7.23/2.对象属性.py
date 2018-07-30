
class DataManager(object):
    def get_total_page(self):
        print('获取总页码数')
class Spider(object):
    def __int__(self):
        # 1.创建一个DataManager对象
        # 2.该对象为Spider的属性
        self.dataManager = DataManager()
    def start_spider(self):
        pass

s = Spider()
s.start_spider()

d = DataManager()
d.get_total_page()