# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Identity(scrapy.Item):
    email_adress = scrapy.Field()
    password = scrapy.Field()
    found_at = scrapy.Field()
    found_url = scrapy.Field()
