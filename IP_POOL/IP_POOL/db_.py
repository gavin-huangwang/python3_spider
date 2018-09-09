import redis
from error import PoolEmptyError
from random import choice

MAX_SCORE = 100
MIN_SCORE = 0
INIT_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

class RedisCliect(object):
	
	def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
		self.db=redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)
	
	def add(self,proxy,score=INIT_SCORE):
		if self.db.zscore(REDIS_KEY ,proxy):
			return self.db.zadd(REDIS_KEY, score, proxy)
			
	def random_proxy(self):
		result=self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
		if len(result):
			return chioce(result)
		else:
			result=self.db.zrevrange(REDIS_KEY, 0, 100)
			if len(result):
				return choice(result)
			else:
				raise PoolEmptyError
				
	def reduce(self, proxy):
		score=self.db.zcore(REDIS_KEY, proxy)
		if score and score > INIT_SCORE:
			return self.db.zincrby(REDIS_KEY, proxy, -1)
		else:
			return self.db.zrem(REDIS_KEY, proxy)
			
	def exists_proxy(self, proxy):
		return not self.db.zscore(REDIS_KEY, proxy) == None
		
	def max(self, proxy):
		return self.db.zadd(REDIS_KEY, MAX_SCORE, proxy)

	def all_proxy(self):
		return self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MIN_SCORE)
	
	def count(self):
		return self.db.zcard(REDIS_KEY)
