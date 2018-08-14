# -*- coding: utf-8 -*-
import scrapy
import re

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5815118868?pn=1']

    def parse(self, response):
        f = open('小说.text','a',encoding='utf-8')
        user_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')

        print('+++++++++++++++++++++++++++++++++++++++++++')
        for user in user_list:
            user_id = user.xpath('.//li[@class="d_name"]/@data-field').extract()[0]
            user_content = user.xpath('.//div[@class="d_post_content j_d_post_content "]').extract()[0]
            if user_id == '{"user_id":2708284572}':
                pattern = re.compile(r'<.*?>',re.S)
                user_content = pattern.sub('',user_content)
                if len(user_content) > 80:
                    print(user_content)
                    f.write(user_content)
        next_page = response.xpath('//li[@class="l_pager pager_theme_5 pb_list_pager"]/a[text()="下一页"]/@href').extract()
        if len(next_page) == 0:
            print('没有下一页了...')
            f.close()
            return
        url = 'https://tieba.baidu.com' + next_page[0]
        print(url)
        yield scrapy.Request(url, callback=self.parse)