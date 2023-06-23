import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import DaftscraperItem
import re
from datetime import datetime

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

        url = response.url
        
        try:
            address = response.css('[data-testid="address"]::text').extract()[0]
        except:
            address = None

        try:
            price_string = response.css('[data-testid="price"] h2::text').extract()[0]
        except:
            price_string = None

        propertytype = response.css('[data-testid="property-type"]::text').extract()[0]

        try:
            beds =  re.findall(r'\d+', response.css('[data-testid="beds"]::text').extract()[0])[0]
        except:
            beds = None

        try:
            baths = re.findall(r'\d+', response.css('[data-testid="baths"]::text').extract()[0])[0]
        except:
            baths = None
            
        description = response.css('[data-testid="description"]::text').extract()[0]

        datelisted = response.css('[data-testid="statistics"] p::text').extract()[0]

        views = int(response.css('[data-testid="statistics"] p::text').extract()[2].replace(',', ''))


        
        
        items['DaftID'] = daftid,
        items['Url'] = url,
        items['Address'] = address,
        items['Price'] = price_string,
        items['Property_Type'] = propertytype,
        items['Beds'] = beds,
        items['Baths'] = baths,
        items['Description'] = description,
        items['Date_Listed'] = datelisted,
        items['Views'] = views

        yield items
