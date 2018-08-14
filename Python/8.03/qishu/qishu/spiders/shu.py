# -*- coding: utf-8 -*-
import scrapy
from ..items import QishuItem

class ShuSpider(scrapy.Spider):
    name = 'shu'
    allowed_domains = ['qisuu.la']
    start_urls = ['https://www.qisuu.la/']

    def parse(self, response):
        # 获取导航页面所有的小说类型
        type_list = response.xpath('//div[@class="nav"]/a/@href').extract()
        # 列表里面第一个是首页 ,将首页去掉
        del type_list[0]
        for type in type_list :
            # 拼接每一个类型的url地址
            # 在这个方法里面 response.url为start_url
            url = response.url + type[1:]
            yield scrapy.Request(url=url,callback=self.get_content_with_type_url)
    # 用来找到每一种类型对应的内容
    def get_content_with_type_url(self,response):
        # 找到类型中第一页所有小说的详情页地址
        book_list = response.xpath('//div[@class="listBox"]/ul/li/a/@href').extract()

        for book in book_list:
            # 在这个方法里面 response.url 为https://qisuu.la/soft/sortX (X)
            url ='https://www.qisuu.la' + book

            yield scrapy.Request(url=url,callback=self.get_detail_with_book_url)
    # 获取每一本书的内容详情
    def get_detail_with_book_url(self,response):
        item = QishuItem()
        # 获取小说标题
        name = response.xpath('//div[@class="detail_right"]/h1/text()').extract()[0]
        print('--------------')
        info_list = response.xpath('//div[@class="detail_right"]/ul/li/text()').extract()

        # 获取需要下载的小说图片地址
        imgUrl = response.xpath('//div[@class="detail_pic"]/img/@src').extract()[0]
        imgUrl = 'https://www.qisuu.la' + imgUrl
        # print(imgUrl)

        downloadUrl = response.xpath('//div[@class="showDown"]/ul/li[3]/script').extract()[0].split(',')[1].strip("'")
        print(downloadUrl)

        item['name'] = [name]
        # 获取小说点击量
        item['clickNum'] = info_list[0]
        # 获取小说大小
        item['fileSize'] = info_list[1]
        # 获取小说类型
        item['bookType'] = info_list[2]
        # 获取小说更新时间
        item['updateTime'] = info_list[3]
        # 获取小说更新状态
        item['bookStatus'] = info_list[4]
        # 获取小说作者
        item['bookAuthor'] = info_list[5]

        item['imageUrl'] = [imgUrl]

        item['downloadUrl'] = [downloadUrl]

        yield item
