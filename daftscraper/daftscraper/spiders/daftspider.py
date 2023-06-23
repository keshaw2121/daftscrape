import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DaftscraperItem

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

        items = DaftscraperItem()

        try:
            daftid = response.css('.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text').extract()[1]
        except:
            daftid = None
        
        try:
            address = response.css('[data-testid="address"]::text').extract()[0]
        except:
            address = None

        price = response.css('[data-testid="price"] h2::text').extract()[0]
        propertytype = response.css('[data-testid="property-type"]::text').extract()[0]

        try:
            beds =  response.css('[data-testid="beds"]::text').extract()[0]
        except:
            beds = 1

        try:
            baths = response.css('[data-testid="baths"]::text').extract()[0]
        except:
            baths = 1
            
        description = response.css('[data-testid="description"]::text').extract()[0]
        datelisted = response.css('[data-testid="statistics"] p::text').extract()[0]
        views = response.css('[data-testid="statistics"] p::text').extract()[2]

        
        
        items['DaftID'] = daftid,
        items['Address'] = address,
        items['Price'] = price,
        items['Property_Type'] = propertytype,
        items['Beds'] = beds,
        items['Baths'] = baths,
        items['Description'] = description,
        items['Date_Listed'] = datelisted,
        items['Views'] = views

        yield items
