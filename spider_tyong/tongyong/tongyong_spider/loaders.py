from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,Join,Compose

class TongyongSpiderItem(ItemLoader):
    default_output_processor = TakeFirst()

class ChinaLoader(TongyongSpiderItem):
    text_out=Compose(Join(),lambda s:s.strip())
    source_out=Compose(Join(),lambda s:s.strip())