from doctest import script_from_examples
from pydispatch import dispatcher
from scrapy import signals



class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
    #    scrapy_item = ScrapyItem()
    #    scrapy_item.unique_id=item['unique_id']
    #    scrapy_item.ticker = item['ticker']
    #    scrapy_item.symbol =    item['symbol']
    #    scrapy_item.date = item['date']
    #    scrapy_item.title = item['title']
    #    scrapy_item.description =item['description']
    #    scrapy_item.importance = item['importance']
    #    scrapy_item.previous = item['previous']
    #    scrapy_item.forecast = item['forecast']
    #    scrapy_item.country = item['country']
    #    scrapy_item.actual = item['actual']
    #    scrapy_item.allDayEvent = item['allDayEvent']
    #    scrapy_item.currency = item['currency']
    #    scrapy_item.reference = item['reference']
    #    scrapy_item.revised = item['revised']
    #    scrapy_item.lastUpdate = item['lastUpdate']
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')