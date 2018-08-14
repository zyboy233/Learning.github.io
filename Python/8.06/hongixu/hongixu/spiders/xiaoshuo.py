# -*- coding: utf-8 -*-
import scrapy
from ..items import HongixuItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/all']
    page = 1

    def parse(self, response):
        if self.page == 26575:
            print('爬完了...')
            return
        # print(response.text)
        li_list = response.xpath('//div[@class="right-book-list"]/ul/li')
        # print(li_list)
        for li in li_list:
            src = li.xpath('.//h3/a/@href').extract()[0]
            src = 'https://www.hongxiu.com' + src
            # print(src)
            yield scrapy.Request(url=src,callback=self.get_sub_page_with_url)
        self.page += 1
        next_page = 'https://www.hongxiu.com/all?pageSize=10&gender=2&catId=30020&isFinish=-1&isVip=-1&size=-1&updT=-1&orderBy=0&pageNum={}'.format(str(self.page))
        yield scrapy.Request(url=next_page,callback=self.parse)
    def get_sub_page_with_url(self,response):
        item = HongixuItem()
        book_info  = response.xpath('//div[@class="book-info"]')
        name = book_info.xpath('.//h1/em/text()').extract()[0]
        info = book_info.xpath('.//p[@class="total"]//text()').extract()
        word_num = info[1] + info[2]
        favor = info[5] + info[6]
        point = info[9] + info[10]
        des_list = book_info.xpath('.//p[@class="intro"]//text()').extract()
        des = ''
        for text in des_list:
            des += text.replace('\s','').replace('\r','')
        img_src ='https:' + response.xpath('//div[@class="book-img"]/a/img/@src').extract()[0]
        item['name'] = name
        item['word_num'] = word_num
        item['favor'] = favor
        item['point'] = point
        item['des'] = des
        item['img_src'] = img_src

        yield item