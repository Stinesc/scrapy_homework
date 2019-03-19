# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jeans_scraping.tasks import add_items


class LordandtaylorPipeline(object):
    current_items = list()

    def process_item(self, item, spider):
        print(self.current_items, 999555)
        self.current_items.append(item)
        if len(self.current_items) >= 1:
            print('dsff')
            add_items(self.current_items)
            self.current_items.clear()
        return item
