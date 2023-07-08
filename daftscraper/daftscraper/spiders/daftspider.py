import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from daftscraper.items import DaftscraperItem
from scrapy.loader import ItemLoader
from datetime import date
from scrapy.exceptions import DropItem

#https://www.daft.ie/property-for-rent/

class DaftspiderSpider(CrawlSpider):
    name = "daftspider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie/"]

    rules = (
        Rule(LinkExtractor(allow = 'property-for-rent')),
        Rule(LinkExtractor(allow = 'for-rent', deny = ['from', 'overseas', 'parking', 'commercial', 'student']), callback = 'parse_item',follow = True)
    )


    def parse_item(self, response):

        address_css = '[data-testid="address"]::text'
        daftid_css = '.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text'
        price_css = '[data-testid="price"] h2::text'
        property_type_css = '[data-testid="property-type"]::text'
        beds_css = '[data-testid="beds"]::text'
        baths_css = '[data-testid="baths"]::text'
        description_css = '[data-testid="description"]::text'
        date_listed_css = '[data-testid="statistics"] p::text'
        views_css = '[data-testid="statistics"] p::text'

        loader = ItemLoader(item = DaftscraperItem(), response = response)
        loader.add_css("daftid", daftid_css, default = 'N/A')

        daft_list = loader.get_collected_values('daftid')
        if len(daft_list) >= 2:
            loader.replace_value('daftid', daft_list[1])

        loader.add_value("date_scraped", date.today())
        loader.add_value("url", response.url)
        loader.add_css("address", address_css)

        loader.add_css("rent_frequency", price_css)

        loader.add_css("price", price_css)
        price_list = loader.get_collected_values('price')
        if len(price_list) >= 2:
            loader.replace_value('price', price_list[0])

        loader.add_css("price_currency", price_css, default = 'N/A')
        loader.add_css("property_type",property_type_css, default = 'N/A')
        loader.add_css("beds", beds_css, default = '1')
        loader.add_css("baths", baths_css, default = '1')
        loader.add_css("description", description_css, default = 'Not available')
        loader.add_css("date_listed", date_listed_css, default = 'N/A')
        loader.add_css("views", views_css, default = 'N/A')

        views_list = loader.get_collected_values('views')
        if len(views_list) >= 4:
            loader.replace_value('views', views_list[2])

        item = loader.load_item()

        if not item.get('address'):
            raise DropItem(f"Data not found in URL: {response.url}")
        
        yield item