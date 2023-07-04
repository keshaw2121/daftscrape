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
        Rule(LinkExtractor(allow = 'property-for-rent')),
        Rule(LinkExtractor(allow = 'for-rent'), callback = 'parse_item', follow = True)
    )


    def parse_item(self, response):

        daftid = '.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text'
        address = '[data-testid="address"]::text'
        price = '[data-testid="price"] h2::text'
        property_type = '[data-testid="property-type"]::text'
        beds = '[data-testid="beds"]::text'
        baths = '[data-testid="baths"]::text'
        description = '[data-testid="description"]::text'
        date_listed = '[data-testid="statistics"] p::text'
        views = '[data-testid="statistics"] p::text'

        loader = ItemLoader(item = DaftscraperItem(), response = response)
        loader.add_css("daftid", daftid)
        loader.add_value("url", response.url)
        loader.add_css("address", address)
        loader.add_css("price", price)
        loader.add_css("property_type",property_type)
        loader.add_css("beds", beds)
        loader.add_css("baths", baths)
        loader.add_css("description", description)
        loader.add_css("date_listed", date_listed)
        loader.add_css("views", views)

        return loader.load_item()