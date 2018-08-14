# -*- coding: utf-8 -*-
import scrapy
from ..items import JobboleItem
from ..items import ArticleItemLoader
from scrapy_redis.spiders import RedisSpider

class BlogSpider(RedisSpider):
    name = 'blog'
    allowed_domains = ['jobbole.com']
    redis_key = 'myspider:start_urls'

    #需求: 获取所有文章的标题,图片地址,时间,详情页地址,收藏,点赞,评论
    def parse(self, response):
        item_list = response.xpath('//div[@class="post floated-thumb"]')
        for item in item_list:
            img = item.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('')
            url = item.xpath('.//a[@class="archive-title"]/@href').extract_first('')
            yield scrapy.Request(url=url,meta={'img':img},callback=self.get_detail_with_url)

        # next_url = response.xpath('.//a[@class="next page-numbers"]').extract()
        # if len(next_url) != 0:
        #     page_url = next_url[0]
        #     yield scrapy.Request(url=page_url,callback=self.parse)

    def get_detail_with_url(self,response):
        # # 图片
        # img = response.meta['img']
        # # 标题
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first('')
        # # 时间
        # date_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first('')
        # date_time = date_time.split('·')[0].strip()
        # # 详情页地址
        # detail = response.url
        # # 点赞
        # dian_zan = response.xpath('//h10/text()').extract_first('')
        # # 收藏数
        # book_mark = response.xpath('//span[@class=" btn-bluet-bigger href-style bookmark-btn  register-user-only "]/text()').extract_first('')
        # book_mark_arry = book_mark.split(' ')
        # book_mark_num = 0
        # if len(book_mark_arry[1]) != 0:
        #     book_mark_num = int(book_mark_arry[1])
        # # 评论
        # comment = response.xpath('//a[@href="#article-comment"]/span/text()').extract_first('')
        # commtent_array = comment.split(' ')
        # comment_num = 0
        # if len(commtent_array[1]) != 0:
        #     comment_num = int(commtent_array[1])
        #
        # item = JobboleItem()
        # item['img'] = img
        # item['title'] = title
        # item['date_time'] = title
        # item['detail'] = detail
        # item['dian_zan'] = dian_zan
        # item['book_mark_num'] = book_mark_num
        # item['comment_num'] = comment_num
        # yield item
        # 创建ItemLoader的实例化对象的时候需要传入两个参数
        # 参数1: item的实例化对象 item里面为还要提取的数据的字段
        # 参数2: 网页的源码
        item_loader = ArticleItemLoader(item=JobboleItem(),response=response)
        # add_value()用于给一个field设置值
        # 后面需要追加两个参数
        # 参数一:设置field的名称
        # 参数二:xpth路径
        item_loader.add_xpath('title','//div[@class="entry-header"]/h1/text()')

        item_loader.add_value('img',response.meta['img'])

        item_loader.add_xpath('date_time','//p[@class="entry-meta-hide-on-mobile"]/text()')

        item_loader.add_value('detail',response.url)

        item_loader.add_xpath('dian_zan','//div[@class="post-adds"]//h10/text()')

        item_loader.add_xpath('book_mark_num','//span[@class=" btn-bluet-bigger href-style bookmark-btn  register-user-only "]/text()')

        item_loader.add_xpath('comment_num','//a[@href="#article-comment"]/span/text()')
        # 将itemloader加载中保存的每一个field数据收集起来
        # 赋值给item对象当中的并且返回到管道
        item = item_loader.load_item()

        yield item