# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaftscraperItem(scrapy.Item):
    DaftID = scrapy.Field()
    Address = scrapy.Field()
    Property_Type = scrapy.Field()
    Price = scrapy.Field()
    Beds = scrapy.Field()
    Baths = scrapy.Field()
    Available_From = scrapy.Field()
    Furnished = scrapy.Field()
    Lease = scrapy.Field()
    Description = scrapy.Field()
    Date_Listed = scrapy.Field()
    Views = scrapy.Field()