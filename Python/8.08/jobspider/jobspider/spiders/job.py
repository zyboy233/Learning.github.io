# -*- coding: utf-8 -*-
import scrapy
from ..items import JobspiderItem

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['search.51job.com']
    start_urls = ['https://search.51job.com/list/170200,000000,0000,00,9,99,java,2,1.html','https://search.51job.com/list/170200,000000,0000,00,9,99,python,2,1.html']

    def parse(self, response):
        div_list = response.xpath('//div[@id="resultList"]/div[@class="el"]')
        # print(div_list)
        for div in div_list:
            # contains 只要属性包含某个值
            jobName = div.xpath('.//p[contains(@class,"t1 ")]/span/a/@title').extract_first('')
            companyName = div.xpath('.//span[@class="t2"]/a/@title').extract_first('')
            cityName = div.xpath('.//span[@class="t3"]/text()').extract_first()
            salary = div.xpath('.//span[@class="t4"]/text()').extract_first('')
            min_salary = 0
            max_salary = 0
            if u'年' in salary:
                money = salary.split('万')[0].split('-')
                min_salary = float(money[0]) / 12
                min_salary = '%.2f' % min_salary
                max_salary = '%.2f' % (float(money[1]) / 12)
            elif u'万' in salary:
                money = salary.split('万')[0].split('-')
                min_salary = money[0]
                max_salary = money[1]
            elif u'千' in salary:
                money = salary.split('千')[0]
                if '-' in money:
                    min_salary = float(money.split('-')[0])*0.1
                    max_salary = float(money.split('-')[1])*0.1
                else:
                    min_salary = 0
                    max_salary = float(money) * 0.1
            elif u'日' in salary:
                money = salary.split('元')
                min_salary = 0
                max_salary = int(money[0]) * 30 /1000
            else:
                min_salary = 0
                max_salary = 0
            date = div.xpath('.//span[@class="t5"]/text()').extract_first()

            item = JobspiderItem()
            item['jobName'] = jobName
            item['companyName'] = companyName
            item['cityName'] = cityName
            item['min_salary'] = min_salary
            item['max_salary'] = max_salary
            item['date'] = date

            yield item
        # next_url = response.xpath('//a[text()="下一页"]/@href').extract()
        # if len(next_url) != 0:
        #     print(next_url[0])
        #     yield scrapy.Request(url=next_url[0],callback=self.parse)
        total_page = int(response.xpath('//div[@class="p_in"]/span/text()').extract_first('').split('共')[1].split('页')[0])
        current_page = int(response.url.split(',').pop(-1).split('.')[0])
        url_list = list(response.url.split(',')[:-1])
        url = ''
        for i in url_list:
            url += i + ','
        if current_page<total_page:
            next_page = url + str(current_page+1) + '.html'
            print(current_page, next_page)
            yield scrapy.Request(url=next_page,callback=self.parse)