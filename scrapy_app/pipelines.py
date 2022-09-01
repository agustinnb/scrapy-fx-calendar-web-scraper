from doctest import script_from_examples
from pydispatch import dispatcher
from scrapy import signals
import psycopg2


class ScrapyAppPipeline(object):
    def __init__(self, unique_id, *args, **kwargs):
        ## Connection to PostgreSQL
        hostname = 'ec2-34-199-68-114.compute-1.amazonaws.com'
        username = 'lzhxopekerjaby'
        password = 'a5e90648b71ebb20a6c5cba94b056bd2e04cb676d54e7f9f7e901c60f86b161f'
        database = 'd8q7q926sob5if'
        port = '5432'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database,port=port)
        self.cur = self.connection.cursor()
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
                ## Define insert statement
        self.cur.execute("""insert into fxcalendar_scrapyitem (unique_id, ticker, symbol, date, title, description, importance, previous, forecast, country, actual, allDayEvent, currency, reference, revised, lastUpdate) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item["unique_id"],
            item["ticker"],
            item["symbol"],
            item["date"],
            item["title"],
            item["description"],
            item["importance"],
            item["previous"],
            item["forecast"],
            item["country"],
            item["actual"],
            item["allDayEvent"],
            item["currency"],
            item["reference"],
            item["revised"],
            item["lastUpdate"]
        ))
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')