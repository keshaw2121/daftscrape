# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy
import re
from itemloaders.processors import TakeFirst, MapCompose
from price_parser import Price
import dateparser
from w3lib.html import remove_tags

def daftid_clean(daftid_var):
    return daftid_var[1]

def address_clean(address_var):
    return address_var[0]

def price_clean(price_var):
    price_var_object = price_var[0]
    return price_var_object

def price_currency(price_var):
    price_var_object = price_var
    price_int = Price.fromString(price_var)
    currency = price_var_object.currency
    return currency

def date_listed_clean(date_listed_var):
    date_listed_object = date_listed_var[0]
    return date_listed_object

def views_clean(views_var):
    views_var_object = views_var[2]
    return views_var_object

def extract_numbers(value):
    pattern = r'\d+'  # Regular expression pattern to match numbers
    matches = re.findall(pattern, value)
    return int(matches[0]) if matches else None



class DaftscraperItem(scrapy.Item):
    daftid = scrapy.Field()

    date_scraped = scrapy.Field()

    url = scrapy.Field()

    address = scrapy.Field()

    price = scrapy.Field(
        input_processor = MapCompose(price_clean)
    )

    property_type = scrapy.Field()

    beds = scrapy.Field()

    baths = scrapy.Field()

    description = scrapy.Field()

    date_listed = scrapy.Field()
    
    views = scrapy.Field()
