# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tongyong_spider.loader_configs import get_config
from tongyong_spider.rules import rules
from tongyong_spider.items import *
from tongyong_spider.loaders import *
from tongyong_spider import urls

class UniversalSpider(CrawlSpider):
    name = 'universal'

    def __init__(self,name,*args,**kwargs):
        config=get_config(name)
        self.config=config
        self.rules=rules.get(config.get('rules'))
        start_urls=config.get('start_urls')
        if start_urls:
            if start_urls.get('type')=='dynamic':
                self.start_urls=list(eval('urls.'+start_urls.get('method'))).[0]
            elif start_urls.get('type')=='static':
                self.start_urls=start_urls.get('value')
        self.allowed_domains=config.get('allowed_domains')
        super(UniversalSpider,self).__init__(*args,**kwargs)


    def parse_item(self, response):
        item=self.config.get('item')
        if item:
            cls=eval(item.get('class'))()
            loader=eval(item.get('loader'))(cls,response=response)
            for key,value in item.get('attrs').items():
                for i in value:
                    if i.get('method')=='xpath':
                        loader.add_xpath(key,*i.get('args'),**{'re':i.get('re')})
                    if i.get('method')=='css':
                        loader.add_css(key,*i.get('args'),**{'re':i.get('re')})
                    if i.get('method')=='value':
                        loader.add_value(key,*i.get('args'),**{'re':i.get('re')})
                    if i.get('method')=='attr':
                        loader.add_value(key,getattr(response,*i.get('args')))
            yield loader.load_item()