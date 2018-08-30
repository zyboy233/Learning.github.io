# -*- coding: utf-8 -*-
import scrapy


class PoSpider(scrapy.Spider):
    name = 'po'
    allowed_domains = ['poro.ws']
    start_urls = ['http://poro.ws/']

    def parse(self, response):
        pass
