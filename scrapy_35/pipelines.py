# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem


class IdentityPipeline(object):

    # check if identitys valid
    def process_item(self, item, spider):
        pass
        # if item['price']:
        #     if item['price_excludes_vat']:
        #         item['price'] = item['price'] * self.vat_factor
        #     return item
        # else:
        #     raise DropItem("Missing price in %s" % item)


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
