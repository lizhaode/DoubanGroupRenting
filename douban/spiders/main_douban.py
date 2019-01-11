import logging

import scrapy

from douban.spiders.lib.SendEMAIL import SendEmail


class MainDouban(scrapy.Spider):
    name = 'DoubanRenting'

    def start_requests(self):
        urls = [
            'https://www.douban.com/group/279962/discussion?start=0',
            'https://www.douban.com/group/sweethome/discussion?start=0',
            'https://www.douban.com/group/26926/discussion?start=0',
            'https://www.douban.com/group/257523/discussion?start=0',
            'https://www.douban.com/group/472358/discussion?start=0'
        ]

        for i in urls:
            yield scrapy.Request(url=i, callback=self.parse)

    def parse(self, response: scrapy.http.response.Response):

        key_words = [
            '望京',
            '望馨花园',
            '望馨园',
            '东湖渠'
        ]

        send = SendEmail()

        page = response.css('td.title')
        for i in page:
            title = i.css('a::text').extract_first().strip()
            link = i.css('a::attr(href)').extract_first()
            self.log('租房标题：{0}'.format(title), level=logging.WARNING)
            self.log('租房链接：{0}'.format(link), level=logging.WARNING)
            email_message = '租房标题：{0}\n租房链接：{1}'.format(title, link)
            for j in key_words:
                if j in title:
                    send.send_email('zhaoli@advance.ai', email_message)
