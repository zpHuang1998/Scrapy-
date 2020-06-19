# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QimoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    unitprice = scrapy.Field()
    maininfo = scrapy.Field()
    subinfo = scrapy.Field()
    area = scrapy.Field()
    xiaoqu = scrapy.Field()
    address = scrapy.Field()
    brokername = scrapy.Field()
    phone = scrapy.Field()