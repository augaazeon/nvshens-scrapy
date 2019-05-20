# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from urllib.parse import urljoin
from Scrapynvshens import items

class StarSpider(Spider):
    name = "star"
    allowed_domains = ["nvshens.com"]
    start_urls = ['https://www.nvshens.com/gallery/4kstar/']

    def parse(self, response):
        page = response.url.split('/')[-1].split('.')[0]   #从url提取页码信息
        if page == '':                                      #首页的URL没有页码
            page = 1
        item_selector = response.xpath('//li[@class="galleryli"]//a[@class="galleryli_link"]/@href')
        for ce,item_url in enumerate(item_selector.extract()):#获取列表页的链接，并用enumerate()生成序号
            yield Request(urljoin('https://www.nvshens.com',item_url),meta = {'page': page, 'ce': ce},callback=self.parse_item)#在响应间传参数page,ce
            # print('url:'+urljoin('https://www.nvshens.com',item_url))
        next_url = response.xpath('//div[@class="pagesYY"]//a[contains(.,"下一页")]/@href').extract_first()#获取下一页的链接
        yield Request(urljoin('https://www.nvshens.com',next_url))

    def parse_item(self,response):
        item = items.StarItem()
        title = response.xpath('//h1[@id="htilte"]/text()').extract_first()
        for info in response.xpath('//ul[@id="hgallery"]//img'):
            item['page'] = response.meta['page']
            item['ce'] = response.meta['ce']
            item['title'] = title
            item['url'] = info.xpath('./@src').extract_first()
            item['alt'] = info.xpath('./@alt').extract_first()
            yield item
        # print('url:'+response.url)
        next_url = response.xpath('//a[contains(.,"下一页")]/@href').extract_first()   #翻页
        yield Request(urljoin('https://www.nvshens.com',next_url),callback=self.parse_item)