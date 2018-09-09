# -*- coding: utf-8 -*-
import scrapy
import json
from hdgtiy.items import HdgtiyItem


class HuizhouSpider(scrapy.Spider):
	name = 'huizhou'
	allowed_domains = ['www.hdgtjy.com']
    #start_urls = ['http://www.hdgtjy.com/']
	#start_urls = []
    #scrapy默认使用get请求，因此需要重写post请求 
	def start_requests(self):
		url='http://www.hdgtjy.com/Index/PublicResults'
		for page in range(1,100):
			form_data={
				'page':str(page),
				'size':'10',
			}
		
		yield scrapy.FormRequest(url,formdata=form_data)

	def parse(self, response):
		item=HdgtiyItem()
		item['js']=response
		print(response)
        
		yield item
			
