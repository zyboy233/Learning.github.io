from urllib.request import Request ,urlopen
import re


class TieBaSpider(object):
    def __init__(self):
        # 基本网址
        self.base_url = 'https://tieba.baidu.com/p/4893709494?pn='
        # 总页码数
        self.total_page = 1
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        self.page_list = []
        self.current_page = 1
    # 2.
    def start_load_url(self  , pageIndex):
        # 3.拼接网址
        full_url = self.base_url + str(pageIndex)
        # 4.设置请求信息
        request = Request(full_url , headers=self.headers)
        # 5.获取响应
        response = urlopen(request)
        try:
            # 6.读取响应内容并且解码
            code = response.read().decode()
        except Exception as e :
            print('请求失败',e)
        else :
            # 7.返回获取的源码
            print('请求第{}页数据成功'.format(self.current_page))
            self.current_page +=1
            return  code

    # 9
    def get_total_page_with_code(self ,code):
        # 10.设置获取总页码的正则
        pattern = re.compile(r'<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)
        # 11.获取总页码
        self.total_page = int(result[0])
    # 获取name和content数据
    def get_content_with_code(self, code):
        # 13
        pattern = re.compile(r'<a.*?class="p_author_name.*?".*?>(.*?)</a>.*?<div.*?class="d_post_content j_d_post_content ".*?>(.*?)</div>',re.S)
        # 14
        result = pattern.findall(code)
        # 15
        self.update_oldData(result)
    # 更新name和content数据
    def update_oldData(self ,oldData):
        remove_element = re.compile(r'<.*?>',re.S)
        space_element = re.compile(r'\s',re.S)
        list = []
        for name , content in oldData :
            sublist = []
            name = re.sub(space_element ,'',name)
            name = name.strip('\n')
            name = re.sub(remove_element ,'',name)

            content = re.sub(space_element,'',content)
            content = content.strip('\n')
            content = re.sub(remove_element,'',content)
            sublist.append(name)
            sublist.append(content)
            list.append(sublist)
            self.page_list = list
        print(self.page_list)
    def spider_manager(self):
        # 1 调用方法
        code = self.start_load_url(self.current_page)
        # 8 调用方法获取总页码
        self.get_total_page_with_code(code)
        # 12.获取每一页的数据
        self.get_content_with_code(code)

        self.get_other_page()

    def get_other_page(self):

        while self.current_page < self.total_page :
            contentString = input('是否请求下一页,回车确定，E退出')
            if contentString == 'E' :
                print('所有数据加载完毕')
                return
                # 1 调用方法
            code = self.start_load_url(self.current_page)
            # 8 调用方法获取总页码
            self.get_total_page_with_code(code)
            # 12.获取每一页的数据
            self.get_content_with_code(code)

tieba = TieBaSpider()
tieba.spider_manager()
