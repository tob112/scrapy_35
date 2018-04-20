# -*- coding: utf-8 -*-
import re

import scrapy
from bs4 import BeautifulSoup
from pprint import pprint

from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider
from scrapy.utils.project import get_project_settings

from scrapy_35.items import Identity


class PastebinSpider(CrawlSpider):
    name = 'pastebin'
    allowed_domains = ['https://pastebin.com/mzXtuFui']
    start_urls = ['https://pastebin.com/mzXtuFui']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:[\S]{4,}$')

        identiies = soup.find_all(text=pattern)

        identity_list = []

        for identity in identiies:
            email = identity.split(":")[0]
            pw = identity.split(":")[1]

            identity_list.append(Identity(email_adress=email, password=pw))

        return identity_list





if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl(PastebinSpider)
    process.start()
