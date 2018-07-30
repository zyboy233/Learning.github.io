from urllib.request import Request,urlopen
import re,sqlite3


class DBManager(object):
    con = sqlite3.connect('okDB')
    cursor = con.cursor()
    isOneInfo = True
    # dbData = None
    @classmethod
    def createTable(cls,info):
        if cls.isOneInfo ==True:
            cls.cursor.execute('create table if not exists spiderTable(value text)')
            cls.con.commit()
        else:
            sqlStr = 'create table if not exists spiderTable('
            for index,value in enumerate(info):
                sqlStr +='value' + str(index) + ' text,'
            sqlStr = sqlStr[0:-1]
            sqlStr += ')'
            cls.cursor.execute(sqlStr)
            cls.con.commit()
            # print(sqlStr)
    @classmethod
    def insert_into(cls,info):
        if cls.isOneInfo ==True:
            cls.cursor.execute('insert into spiderTable VALUES "{}" '.format(info))
            cls.con.commit()
        else:
            # 多条数据拼接
            sqlStr = 'insert into spiderTable('
            key = ''
            values = ' values('
            for index,value in enumerate(info):
                key += 'value' + str(index) +' ,'
                values +='"' + info[index] +  '"' +' ,'
            key = key[0:-1]
            key += ')'

            values = values[0:-1]
            values +=')'
            # print(key)
            # print(value)
            sqlStr += key + values
            print(sqlStr)
            cls.cursor.execute(sqlStr)
            cls.con.commit()
class DataManager(object):
    # 根据源码获取指定的内容
    @classmethod
    def get_info_with_code(cls,code,pattern):
        # print(code)
        pattern = re.compile(r'{}'.format(pattern),re.S)
        result = pattern.findall(code)
        print(result)

        return result
    @classmethod
    def change_data_with(cls,old_data):
        # 如果获取的时一条数据,那么这条数据类型是字符串,会被放入到列表中
        # 如果获取的是多条数据,那么每条数据都是元组,也会被放入列表中
        space = re.compile(r'\s', re.S)
        element = re.compile(r'<.*?>', re.S)
        if type(old_data) == str:
            old_data = old_data.strip('\n')
            old_data = re.sub(space,'',old_data)
            old_data = re.sub(element,'',old_data)
            DBManager.isOneInfo = True
            return old_data
        else:
            list = []
            for content in old_data:
                print(content)
                content = content.strip('\n')
                content = space.sub('',content)
                content = element.sub('',content)
                list.append(content)
            # print(list)
            DBManager.isOneInfo = False
            return list
class Spider(object):
    def __init__(self,base_url,pattern):
        self.base_url = base_url
        self.pattern = pattern
        self.headers = headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    def load_url(self):
        url = self.base_url+'1'
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求首页出错',e)
        else:
            # print(code)
            result_list = DataManager.get_info_with_code(code,self.pattern)
            for value in result_list:
                # 字符串 或者 元组
                newData = DataManager.change_data_with(value)
                # 创建数据表
                DBManager.createTable(newData)
                # 插入数据
                DBManager.insert_into(newData)


spider = Spider('https://www.qiushibaike.com/hot/page/','<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>')
spider.load_url()