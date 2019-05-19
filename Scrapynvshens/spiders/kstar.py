# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KstarSpider(CrawlSpider):
    name = 'kstar'
    allowed_domains = ['www.nvshens.com']
    start_urls = ['http://www.nvshens.com/gallery/4kstar//']
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@class="galleryli"]//a[@class="galleryli_link"]'), callback='parse_item',follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pagesYY"]//a[contains(.,"下一页")]'))
    )
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
