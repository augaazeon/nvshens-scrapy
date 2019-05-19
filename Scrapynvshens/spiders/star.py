# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from urllib.parse import urljoin
from Scrapynvshens import items

class StarSpider(Spider):
    name = "star"
    allowed_domains = ["nvshens.com"]
    start_urls = ['https://www.nvshens.com/gallery/4kstar/']

    def parse(self, response):
        page = response.url.split('/')[-1].split('.')[0]
        if page == '':
            page = 1
        item_selector = response.xpath('//li[@class="galleryli"]//a[@class="galleryli_link"]/@href')
        for ce,item_url in enumerate(item_selector.extract()):
            yield Request(urljoin('https://www.nvshens.com',item_url),meta={'page':page,'ce':ce},callback=self.parse_item)
            # print('url:'+urljoin('https://www.nvshens.com',item_url))
        next_url = response.xpath('//div[@class="pagesYY"]//a[contains(.,"下一页")]/@href').extract_first()
        yield Request(urljoin('https://www.nvshens.com',next_url))

    def parse_item(self,response):
        item = items.StarItem()

        ab = response.xpath('//ul[@id="hgallery"]//img')
        title = response.xpath('//h1[@id="htilte"]/text()').extract_first()
        for info in ab:
            item['page'] = response.meta['page']
            item['ce'] = response.meta['ce']
            item['title'] = title
            item['url'] = info.xpath('.//@src').extract_first()
            item['alt'] = info.xpath('.//@alt').extract_first()
            yield item
        # print('url:'+response.url)
        next_url = response.xpath('//a[contains(.,"下一页")]/@href').extract_first()
        yield Request(urljoin('https://www.nvshens.com',next_url),callback=self.parse_item)