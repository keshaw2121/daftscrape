import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DaftscraperItem
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join

#https://www.daft.ie/property-for-rent/

class DaftspiderSpider(CrawlSpider):
    name = "daftspider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie/"]

    rules = (
        Rule(LinkExtractor(allow = 'property-for-rent'), deny = ['overseas-properties-for-rent', 'parking-spaces-for-rent']),
        Rule(LinkExtractor(allow = 'for-rent'), callback = 'parse_item', follow = True)
    )


    def parse_item(self, response):

        l = ItemLoader(item = DaftscraperItem(), response = response)
        l.add_css("DaftID", '.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text')
        l.add_value("Url", response.url)
        l.add_css("Address", '[data-testid="address"]::text')
        l.add_css("Price", '[data-testid="price"] h2::text')
        l.add_css("Property_Type",'[data-testid="property-type"]::text')
        l.add_css("Beds", '[data-testid="beds"]::text')
        l.add_css("Baths", '[data-testid="baths"]::text')
        l.add_css("Description", '[data-testid="description"]::text')
        l.add_css("Date_Listed", '[data-testid="statistics"] p::text')
        l.add_css("Views", '[data-testid="statistics"] p::text')

        return l.load_item()
