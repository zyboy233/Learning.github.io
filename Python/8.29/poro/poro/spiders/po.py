# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class PoSpider(scrapy.Spider):
    name = 'po'
    allowed_domains = ['poro.ws']
    start_urls = ['http://poro.ws/']
    def __init__(self):
        self.driver = webdriver.Chrome()
    def parse(self, response):
        pass
