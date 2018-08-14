# -*- coding: utf-8 -*-
import scrapy
import re


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5815118868?pn=1']
    f = open('tieba.txt','a',encoding='utf-8')

    def parse(self, response):
        # 找到指定div标签 为贴吧内容和作者的集合体
        div_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # 找到作者
        for div in div_list:
            # 获取含有louzhubiaoshi.wrap类名的标签
            # 该类名只有楼主才有
            author = div.xpath('.//div[@class="louzhubiaoshi_wrap"]').extract()
            if len(author) != 0:
                # 获取标签内部全部文本的几种方式
                # 1.获取最外边标签,遍历内部所有子标签,获取标签文本
                content =div.xpath('.//cc/div[@class="d_post_content j_d_post_content "]//text()').extract()
                # 2.正则去掉所有标签 <.*?>      re.sub('',content)
                # content = div.xpath('.//cc/div[@class="d_post_content j_d_post_content "]')
                # pattern = re.compile('<.*?>')
                # content = pattern.sub('',content)
                # 3./text() 获取标签的文本   //text()获取标签以及子标签的文本
                content_list = div.xpath('.//div[@class="d_post_content j_d_post_content "]//text()').extract()
                # 4.使用xpath('string(.)')这种方式获取所有文本 并且拼接
                # content = div.xpath('.//div[@class="d_post_content j_d_post_content "]').xpath('string(.)').extract()[0] + '\n'
                print(content)
                remove = re.compile('\s')
                content = ''
                for string in content_list:
                    string = remove.sub('',string)
                    content += string
                self.f.write(content + '\n')