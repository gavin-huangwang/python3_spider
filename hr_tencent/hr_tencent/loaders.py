from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class HrTencentItem(ItemLoader):
    default_output_processor = TakeFirst()
    
class TenLoader(HrTencentItem):
    pass
