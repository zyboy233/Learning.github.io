from urllib.request import Request,urlopen
import re, sqlite3

# 获取贴吧的内容存到数据库
# a.拼接url(拼接后要获取一共多少页)
#     > 注意url规律
# b.拼接后获取网页源码 code
#     > 用不用代理ip User-Agent  注意源码内容
# c.分离数据(pettern)
#     > 注意源码中是否有该数据 正则
# d.存储到数据库
#     > 是否连接到数据库 游标是否初始化 数据库格式
# e.如果数据属于楼主,则同时存储到txt
#     > 'w','a','r'

class DBManager(object):
    con = sqlite3.connect('tieBa')
    cursor = con.cursor()
    @classmethod
    def create_table(cls):
        cls.cursor.execute('create table if not exists tieBaTable(name text,content text)')
        cls.con.commit()
    @classmethod
    def insert_into_table(cls,receive_name,receive_content):
        cls.cursor.execute('insert into tieBaTable VALUES ("{}","{}")'.format(receive_name,receive_content))
        cls.con.commit()
    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.con.close()
# data 数据 manager 管理
class DataManager(object):
    def __init__(self):
        self.code = '1'
    def get_total_page(self,code):
        # 注意: 代码执行到这的时候self.code就被赋值了
        self.code = code
        pattern = re.compile(r'<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)[0]
        # 将result 值的返回给调用者
        return result
        print(result)
    def get_name_and_content(self):
        pattern = re.compile(r'<a.*?class="p_author_name.*?".*?>(.*?)</a>.*?<div.*?class="d_post_content j_d_post_content ">(.*?)</div>',re.S)
        result = pattern.findall(self.code)
        print(result)
        space_content = re.compile(r'\s',re.S)
        italic_content = re.compile(r'\u3000',re.S)
        #去除任意标签
        br_content = re.compile(r'<.*?>',re.S)
        for name,content in result:
            # 去除换行
            name = name.strip('\n')
            # 去除空格
            name = re.sub(space_content, '', name)
            name = re.sub(italic_content, '', name)
            # 去除标签
            name = re.sub(br_content, '', name)

            content = content.strip('\n')
            content = re.sub(space_content,'',content)
            content = re.sub(italic_content,'',content)
            content = re.sub(br_content,'',content)
            # print(name)
            # print(content)

            DBManager.insert_into_table(name,content)

            if name == "恶人能活一世纪" and len(content)>150:
                with open('text.txt','a',encoding='utf-8')as f:
                    f.write(content)
                    f.close()

class TiebaSpider(object):
    def __init__(self):
        self.base_url = 'https://tieba.baidu.com/p/4685013359?pn='
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # 将数据管理作为自己的属性
        self.dataManager = DataManager()
        self.total_page = '1'
        self.current_page = 1
    def start_spider(self,pageIndex):
        url = self.base_url + str(pageIndex)
        # 拼接url 封装请求
        request = Request(url,headers=self.headers)
        # 获取响应
        response = urlopen(request)
        # 读取获取的内容并解码
        result = response.read().decode()
        # 将所有的数据传给dataManager对象的get_total_page方法
        # 如果代码中要调用其他的方法 那么先执行其他方法里面的代码
        # 然后继续执行
        self.total_page = self.dataManager.get_total_page(result)
        # print(result)
        print('-------------------------------')
        # 代码执行到这:获取源码,分离数据,存入数据库完成
        self.dataManager.get_name_and_content()

        if self.current_page < int(self.total_page):
            self.current_page+=1
            self.start_spider(self.current_page)
        else:
            DBManager.close()

DBManager.create_table()
tieba = TiebaSpider()

tieba.start_spider(1)
