# -*- coding: utf-8 -*-
import scrapy

# 在同级文件夹路径下 找到制定的文件items
# 所以要回到上级文件夹来找 ..回到上级路径
from ..items import MokoItem
class MeikongSpider(scrapy.Spider):
    name = 'meikong'
    allowed_domains = ['moko.cc']
    # 通常会修改爬虫程序的start_urls
    start_urls = ['http://www.moko.cc/channels/post/153/1.html']

    def parse(self, response):
        # print(response.text)
        ul_list = response.xpath('//ul[@class="post small-post"]')
        # print(ul_list)
        for ul in ul_list:
            # 初始化一个对象
            item = MokoItem()
            # xpath获取的内容 都是一个了列表
            # 返回的内容为 scrapy.selector
            # 如果对象类型为scrapy.selector 那么这个对象可以被继续迭代
            # 也可以被xpath继续寻找里面的对象
            title = ul.xpath('.//div[@class="cover"]/@cover-text')[0]
            # print(title)
            # print(type(title))
            title = title.extract()
            # print(title) # ['美轮美奂']
            # 如果这个对象类型为list 那么这个对象可以被迭代
            #  但是不能继续使用xpath
            # print(type(title)) # <class list>

            # 点击量
            clickNum = ul.xpath('.//li[last()]/span/text()').extract()[0]

            # 图片链接
            imgSrc = ul.xpath('.//img/@src2').extract()[0]

            item['title'] = u'{}'.format(title)
            item['imgSrc'] = u'{}'.format(imgSrc)
            item['clickNum'] = u'{}'.format(imgSrc)

            # 将文件存储为指定类型 支持四种数据类型text,json,xml,csv
            # crapy crwl meikong -o meikong.xml

            # 转换编码
            # scrapy crawl meikong -o mei.json -s FEED_EXPORT_ENCODING=UTF-8

            yield item

        # yield 的作用 return
        # yield all_items

