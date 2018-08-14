# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
import scrapy
from scrapy.exceptions import DropItem

class ZhixuanPipeline(object):
    def process_item(self, item, spider):
        return item

class MyFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['src']:
            yield scrapy.Request(file_url,meta={'item':item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        FolderName = 'haha'
        file_guid = item['name']
        filename = u'{0}/{1}.rar'.format(FolderName,file_guid)
        return filename

    def item_completed(self, results, item, info):
        print(results)
        print(item)
        file_paths = [x['path'] for ok, x in results if ok]
        print(file_paths)
        if not file_paths:
            raise DropItem("Item contains no files")
        # item['file_paths'] = file_paths
        return item




