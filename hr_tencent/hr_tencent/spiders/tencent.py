# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hr_tencent.items import *
from scrapy.loader import ItemLoader
#from hr_tencent.loaders import *


class TencentSpider(CrawlSpider):
	name = 'tencent'
	allowed_domains = ['hr.tencent.com']
	start_urls = ['https://hr.tencent.com/position.php']

	rules = (
		Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
		Rule(LinkExtractor(allow=r'position_detail\.php?'), callback='parse_item', follow=True),
		)

	def parse_item(self, response):
		loader=ItemLoader(item=HrTencentItem(),response=response)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
		loader.add_value('domain','hr.tencent.com')
		loader.add_xpath('all_adress','//*[@id="additems"]')
		loader.add_xpath('all_type','//*[@id="searchrow3"]/div[contains(@class,"left items pl9")]')
		loader.add_xpath('work','//*[@id="sharetitle"]/text()')
		loader.add_xpath('work_type','//*[@id="position_detail"]//tr[contains(@class,"bottomline")]/td[2]')
		loader.add_xpath('num','//*[@id="position_detail"]//tr[contains(@class,"bottomline")]/td[3]')
		loader.add_xpath('adress','//*[@id="position_detail"]//tr[contains(@class,"bottomline")]/td[1]')
		loader.add_xpath('time','//*[@id="position"]//tr[*]//td[5]')
		loader.add_xpath('text','//*[@id="position_detail"]/div/table[contains(@class,"tablelist")]')
        
		yield loader.load_item()
