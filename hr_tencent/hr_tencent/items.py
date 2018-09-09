# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HrTencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    domain = scrapy.Field()
    all_adress = scrapy.Field()
    all_type = scrapy.Field()
    work = scrapy.Field()
    work_type = scrapy.Field()
    num = scrapy.Field()
    adress = scrapy.Field()
    time = scrapy.Field()
    text = scrapy.Field()
    
