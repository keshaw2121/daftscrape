# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaftscraperItem(scrapy.Item):
    DaftID = scrapy.Field()
    Url = scrapy.Field()
    Address = scrapy.Field()
    Price = scrapy.Field()
    Property_Type = scrapy.Field()
    Beds = scrapy.Field()
    Baths = scrapy.Field()
    Description = scrapy.Field()
    Date_Listed = scrapy.Field()
    Views = scrapy.Field()
