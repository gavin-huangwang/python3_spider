# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from baidutieba.items import BaidutiebaItem
import json


class TiebaSpider(scrapy.Spider):
	name = 'tieba'
	allowed_domains = ['tieba.baidu.com']
	for page in range(0,100,50):
		kw='网络爬虫'
		url='https://tieba.baidu.com/f?kw='+parse.quote(kw)+'&ie=utf-8&pn='+str(page)
		start_urls = [url]

	def parse(self, response):
		quotes=response.xpath('//*[@id="thread_list"]')
		for quote in quotes:
			print(quote)
			item=BaidutiebaItem()
			item['title']=quote.xpath('.//a[contains(@class,"j_th_tit")]/text()').extract()
			item['text']=quote.xpath('.//div[contains(@class,"threadlist_abs")]').extract()
			item['autour']=quote.xpath('.//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
			item['time']=quote.xpath('.//span[contains(@class,"threadlist_reply_date")]/text()').extract()
			item['reply']=quote.xpath('//span[contains(@class,"threadlist_rep_num")]/text()').extract()
		yield item
			
        
