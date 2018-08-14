# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response import Response

class SeleniumSpiderMiddleware(object):

    def process_request(self,request,spider):
        # 当引擎从调度器取出request进行请求发送下载器之前
        # 会先执行当前的爬虫中间件,在中间件里面使用selenium
        # 请求这个request,拿到动态网站的数据,然后将请求返回给
        # spider爬虫对象
        print('++++++++++++++++++++++++++++++')
        if spider.name == 'taobao':
            # 使用爬虫文件的地址
            spider.driver.get(request.url)
            for x in range(1,12,2):
                i = float(x) / 11
                js = 'document.body.scrollTop=document.body.scrollHeight * %f' % i
                spider.driver.execute_script(js)
            # 设置响应信息,响应的url为请求的url,响应的网页内容为请求网页的源码
            # 响应的编码为utf-8 请求的信息为获取的信息
            response = HtmlResponse(url=request.url,body=spider.driver.page_source,encoding='utf-8',request=request)

            # 这个地方只能返回response
            # 如果返回了response对象
            # 那么可以直接跳过下载中间件
            # 将response的值传递给引擎
            # 引擎有传递给spider进行解析
            print('+++++++++++++--------------------')
            return response
class TaobaospiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TaobaospiderDownloaderMiddleware(object):
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
