import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://www.daft.ie/property-for-rent/

class DaftspiderSpider(CrawlSpider):
    name = "daftspider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie/"]

    rules = (
        Rule(LinkExtractor(allow='property-for-rent'), follow = True),
        Rule(LinkExtractor(allow='for-rent'), callback='parse_item', follow = True)
    )




    def parse_item(self, response):
            daftid = response.css('.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text').extract()[1]
            url = response.url
            address = response.css('[data-testid="address"]::text').get()
            propertytype = response.css('[data-testid="property-type"]::text').get(),
            price = response.css('[data-testid="price"] h2::text').getall()[0]
            beds = response.css('[data-testid="beds"]::text').get()
            baths = response.css('[data-testid="baths"]::text').get()
            availablefrom = response.css('[data-testid="overview"] li::text').getall()[5]
            furnished = response.css('[data-testid="overview"] li::text').getall()[7]
            lease = response.css('[data-testid="overview"] li::text').getall()[9]
            description = response.css('[data-testid="description"]::text').get()
            datelisted = response.css('[data-testid="statistics"] p::text').get()
            views = response.css('[data-testid="statistics"] p::text').getall[2]

            yield {
                'DaftID' : daftid,
                'Url' : url,
                'Address' : address,
                'Property_Type' : propertytype,
                'Price' : price,
                'Beds' : beds,
                'Baths' : baths,
                'Available_From' : availablefrom,
                'Furnished' : furnished,
                'Lease' : lease,
                'Description' : description,
                'Date' : datelisted,
                'Views' : views
            }
