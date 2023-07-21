import scrapy


class DaftstudiospiderSpider(scrapy.Spider):
    name = "daftstudiospider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie/"]

    def parse(self, response):
        pass
