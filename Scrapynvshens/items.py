# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

class StarItem(Item):
    #4k
    collection = 'star'
    image_paths = Field()
    page = Field()  #页码
    ce =Field()     #某页的第几册
    url = Field()   #单张图片的URL
    alt = Field()   #单张图片的alt信息
    title = Field() #图册的目录，存储图片时作为文件夹名