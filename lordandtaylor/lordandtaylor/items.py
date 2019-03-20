# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LordandtaylorItem(scrapy.Item):

    title = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    sizes = scrapy.Field()
    description = scrapy.Field()
    color = scrapy.Field()
