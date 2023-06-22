import scrapy

#https://www.daft.ie/property-for-rent/

class DaftspiderSpider(CrawlSpider):
    name = "daftspider"
    allowed_domains = ["www.daft.ie"]
    start_urls = ["https://www.daft.ie/for-rent/house-38a-beechwood-avenue-lower-dublin-6-ranelagh-dublin-6/5294088"]



    def parse(self, response):

        items = DaftscraperItem()

        daftid = response.css('.DaftIDText__StyledDaftIDParagraph-vbn7aa-0::text').extract()[1]
        address = response.css('[data-testid="address"]::text').extract()[0]
        price = response.css('[data-testid="price"] h2::text').extract()[0]
        propertytype = response.css('[data-testid="property-type"]::text').extract(),
        beds = response.css('[data-testid="beds"]::text').extract()[0]
        baths = response.css('[data-testid="baths"]::text').extract()[0]
        avaialablefrom = response.css('[data-testid="overview"] li::text').getall()[5]
        furnished = response.css('[data-testid="overview"] li::text').getall()[7]
        lease = response.css('[data-testid="overview"] li::text').getall()[9]
        description = response.css('[data-testid="description"]::text').extract()
        datelisted = response.css('[data-testid="statistics"] p::text').extract()[0]
        views = response.css('[data-testid="statistics"] p::text').extract()[2]

        items['DaftID'] = daftid,
        items['Address'] = address,
        items['Price'] = price,
        items['Property_Type'] = propertytype,
        items['beds'] = beds,
        items['baths'] = baths,
        items['Available_From'] = avaialablefrom,
        items['Furnished'] = furnished,
        items['Lease'] = lease,
        items['Description'] = description,
        items['Date_Listed'] = datelisted,
        items['Views'] = views

        yield items
