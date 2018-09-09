# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem
from urllib .request import Request

class LagouJobSpider(scrapy.Spider):
	name = 'lagou_job'
	allowed_domains = ['www.lagou.com']
	start_urls = ['http://www.lagou.com/']
	
	def start_requests(self):
		url='https://www.lagou.com/jobs/4632901.html'
		headers={
		'accept-language': 'zh-CN,zh;q=0.8',
		'user-agent': 'Mozilla/5.0 (Windows NT 6.3)',
		}
		yield scrapy.Request(url,headers=headers,callback=self.parse)
		
	def parse(self, response):
		item=LagouItem()
		item['company']=response.xpath('//div[contains(@class,"position-content-l")]//div[(@class="company")]').extract()
		item['work']=response.xpath('//div[contains(@class,"position-content-l")]//span[(@class="name")]').extract()
		item['salary']=response.xpath('//div[@class="position-content-l"]//dd[@class="job_request"]//span[1]').extract()
		item['condition']=response.xpath('//div[@class="position-content-l"]//dd[@class="job_request"]//span[position()>1]/text()').extract()
		item['label']=response.xpath('//div[@class="position-content-l"]//ul[contains(@class,"position-label")]/li/text()').extract()
		item['time']=response.xpath('//div[@class="position-content-l"]//p[contains(@class,"publish_time")]/text()').extract_first()
		item['advantage']=response.xpath('//*[@id="job_detail"]//dd[@class="job-advantage"]').extract()
		item['description']=response.xpath('//*[@id="job_detail"]//dd[@class="job_bt"]').extract()
		item['address']=response.xpath('//*[@id="job_detail"]//dd[contains(@class,"job-address")]').extract()
		yield item
		
        
