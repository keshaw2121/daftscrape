import scrapy


class DaftspiderSpider(scrapy.Spider):
    name = "daftspider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie"]

    def parse(self, response):
        pass
