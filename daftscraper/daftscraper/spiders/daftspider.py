import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DaftscraperItem
from scrapy.loader import ItemLoader
from datetime import date

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

        daftid_css = '.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text'
        address_css = '[data-testid="address"]::text'
        price_css = '[data-testid="price"] h2::text'
        property_type_css = '[data-testid="property-type"]::text'
        beds_css = '[data-testid="beds"]::text'
        baths_css = '[data-testid="baths"]::text'
        description_css = '[data-testid="description"]::text'
        date_listed_css = '[data-testid="statistics"] p::text'
        views_css = '[data-testid="statistics"] p::text'

        loader = ItemLoader(item = DaftscraperItem(), response = response)
        loader.add_css("daftid", daftid_css)
        loader.add_value("date", date.today())
        loader.add_value("url", response.url)
        loader.add_css("address", address_css)
        loader.add_css("price", price_css)
        loader.add_css("property_type",property_type_css)
        loader.add_css("beds", beds_css)
        loader.add_css("baths", baths_css)
        loader.add_css("description", description_css)
        loader.add_css("date_listed", date_listed_css)
        loader.add_css("views", views_css)

        return loader.load_item()