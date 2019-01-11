import logging

import scrapy


class MainDouban(scrapy.Spider):
    name = 'DoubanRenting'

    def start_requests(self):
        urls = [
            'https://www.douban.com/group/279962/discussion?start=0',
            'https://www.douban.com/group/sweethome/discussion?start=0'
        ]

        for i in urls:
            yield scrapy.Request(url=i, callback=self.parse)

    def parse(self, response):
        page = response.css('td.title')
        for i in page:
            title = i.css('a::text').extract_first().strip()
            self.log('lizhao==>{0}'.format(title), level=logging.WARNING)
