# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
# 爬虫中间件 设置在请求过程中的信息
class BaiduspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    # 创建爬虫时调用
    def from_crawler(cls, crawler):
        print('爬虫创建')
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
    # 处理下载器返回的response对象
    def process_spider_input(self, response, spider):
        print('in函数被执行')
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None
    # 当response对象被spider解析完成后,返回结果经过这个函数
    def process_spider_output(self, response, result, spider):
        print('out函数被执行')
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i
    # 当爬虫的中间件出现异常的时候被调用
    def process_spider_exception(self, response, exception, spider):
        print('爬虫出现异常')
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass
    # 当爬虫开始的时候 从start_urls中发起request
    def process_start_requests(self, start_requests, spider):
        print('start_url请求启动')
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r
    # 当爬虫程序启动的时候执行
    def spider_opened(self, spider):
        print('爬虫程序启动')
        spider.logger.info('Spider opened: %s' % spider.name)

"""
1.请求在开始的时候,会优先从settings里面找User-Agent,如果里面没有设置
会有一个默认的'User-Agent':'scrapy'
2.设置User-Agent的另外一种方式 就是在这里设置
scrapy内部会启动一个爬虫中间件 UserAgentMiddleware 设置请求信息的话
需要在这里面设置,因此此中间件包含了一个
"""

class RandomUserAgentMiddleware(object):
    def __init__(self,crawler):
        super(RandomUserAgentMiddleware).__init__()
        self.ua = UserAgent()
        # 从配置文件settings中读取Random_ua_type值,如果不存在
        # 则采用默认的random进行随机
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')
    # 创建爬虫开始的方法
    # 注意: 方法和参数必须和系统方法和参数保持一致
    @classmethod
    def from_crawler(cls,crawler):
        # 返回当前response的对象
        print('user-agent111111111111111111111111111')
        return cls(crawler)
    # 当进程进行请求的时候
    def process_request(self,request,spider):
        print('user-agent22222222222222222222222222222')
        def user_agent():
            return getattr(self.ua,self.ua_type)
        request.headers.setdefault('User-Agent',user_agent())
# 下载中间件 设置下载文件信息
class BaiduspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
