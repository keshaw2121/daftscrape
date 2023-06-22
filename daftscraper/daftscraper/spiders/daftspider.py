import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://www.daft.ie/property-for-rent/

class DaftspiderSpider(CrawlSpider):
    name = "daftspider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie/"]

    def parse(self, response):
        daftid = response.css('.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text').extract()[1]
        address = response.css('[data-testid="address"]::text').extract()[0]
        price = response.css('[data-testid="price"] h2::text').extract()[0]
        propertytype = response.css('[data-testid="property-type"]::text').extract(),
        beds = response.css('[data-testid="beds"]::text').extract()[0]
        baths = response.css('[data-testid="baths"]::text').extract()[0]
        availablefrom = response.css('[data-testid="overview"] li::text').getall()[5]
        furnished = response.css('[data-testid="overview"] li::text').getall()[7]
        lease = response.css('[data-testid="overview"] li::text').getall()[9]
        description = response.css('[data-testid="description"]::text').extract()
        datelisted = response.css('[data-testid="statistics"] p::text').extract()[0]
        views = response.css('[data-testid="statistics"] p::text').extract()[2]

        yield {
            'DaftID' : daftid,
            'Address' : address,
            'Price' : price,
            'Property_Type' : propertytype,
            'Beds' : beds,
            'Baths' : baths,
            'Available_From' : availablefrom,
            'Furnished' : furnished,
            'Lease' : lease,
            'Description' : description,
            'Date' : datelisted,
            'Views' : views
        }
