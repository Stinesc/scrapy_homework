# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jeans_scraping.tasks import add_items


class LordandtaylorPipeline(object):

    def __init__(self):
        self.items_list = list()
        self.items_limit = 20

    def process_item(self, item, spider):
        self.items_list.append(dict(item))
        if len(self.items_list) >= self.items_limit:
            add_items.delay(self.items_list)
            self.items_list = list()

    def close_spider(self, spider):
        add_items.delay(self.items_list)
