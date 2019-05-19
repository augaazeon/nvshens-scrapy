# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
            referer=item['url']  # 处理防盗链
            yield Request(item['url'],meta={'item': item,'referer':referer})#配合get_media_requests传递meta，不然拿不到item的.不会下载

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        folder = item['title']
        folder_strip = folder.strip()
        image_guid = request.url.split('/')[-1]
        filename = u'{0}/{1}'.format(folder_strip, image_guid)
        return filename

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        # item['image_paths'] = image_path
        return item
