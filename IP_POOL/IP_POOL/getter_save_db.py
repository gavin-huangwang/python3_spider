from db_ import RedisCliect
from crawl_ import Crawler

POOL_UPPER_THRESHOLD = 10000

class Getter():
	def __init__(self):
		self.redis = RedisCliect()
		self.crawler = Crawler()
	
	def is_over_threshold(self):
		if self.redis.count >= POOL_UPPER_THRESHOLD:
			return True
		else:
			return False
			
	def run(self):
		if not self.is_over_threshold:
			for callback_lab in range(self.crawler.__CrawlFuncCount__):
				callback=self.crawler.__CrawlFunc__[callback_lab]
				proxies=self.crawler.get_proxy(callback)
				for proxy in proxies:
					self.redis.app(proxy)


