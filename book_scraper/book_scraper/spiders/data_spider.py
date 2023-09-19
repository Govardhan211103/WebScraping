import scrapy


class DataSpiderSpider(scrapy.Spider):
    name = "data_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        pass
