import asyncio
import aiohttp
import time
from db_ import RedisCliect
STATUS_CODES = [200]
TEST_URL = None
BATCH_TEST_SIZE =100

class Tester(object):
	def __init__(self):
		self.redis=RedisCliect()
	
	async def test_one_proxy(self, proxy):
		conn = aiohttp.TCPConnector(verify_ssl = False)
		async with aiohttp.ClientSession(connect = conn) as session:
			try:
				if isinstance(proxy, bytes):
					proxy = proxy.decode('utf-8')
				real_proxy = 'http://'+proxy
				async with session.get(TEST_URL, proxy=real_proxy, timeout=20) as response:
					if  response.status in STATUS_CODES:
						self.redis.max(proxy)
					else:
						self.redis.reduce(proxy)
			except (ClientError, ClientConnectorError, TimeoutError, AttributeError):
				self.redis.reduce(proxy)
	
	def run(self):
		try:
			proxies = self.redis.all_proxy()
			loop = asyncio.get_event_loop()
			for i in range(0, len(proxies), BATCH_TEST_SIZE):
				test_proxies = proxies[i:i + BATCH_TEST_SIZE]
				tasks=[self.test_one_proxy(proxy) for proxy in test_proxies]
				loop.run_until_complete(asyncio.wait(tasks))
				time.sleep(5)
		except Exception as e:
			print('test error',e.args)
