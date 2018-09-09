from scrapy import cmdline
def run():
	cmdline.execute('scrapy crawl tencent -o tencent.json'.split())
	
if __name__=='__mian__':
	run()
 
