import sys
from scrapy.utils.project import get_project_settings
from tongyong_spider.spiders.universal import UniversalSpider
from tongyong_spider.loader_configs import get_config
from scrapy.crawler import CrawlerProcess

def run():
    name=sys.argv[1]
    zidyi_settings=get_config(name)
    spider=zidyi_settings.get('spider','universal')
    project_settings=get_project_settings()
    settings=dict(project_settings.copy())
    settings.update(zidyi_settings.get('settings'))
    process=CrawlerProcess(settings)
    process.crawl(spider,**{'name':name})
    process.start()


if __name__=='__main__':
    run()
