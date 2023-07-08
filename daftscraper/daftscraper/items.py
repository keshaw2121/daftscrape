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


def extract_number(string):
    pattern = r'\d+'  # Regular expression pattern to match one or more digits
    numbers = re.findall(pattern, string)
    combined_number = ''.join(numbers)
    return combined_number

def get_currency(price):
    price_object = Price.fromstring(price)
    currency = price_object.currency
    return currency

def description_clean(description):
    description_object = description.replace('\n', '').replace('\r', '').replace('*', '').replace('///', '').replace('\t', '')
    return description_object

def extract_frequency(text):
    pattern = r'per\s+(week|month)'
    match = re.search(pattern, text, flags=re.IGNORECASE)
    
    if match:
        frequency = match.group(1).lower()
        
        if frequency == 'week':
            return 'weekly'
        elif frequency == 'month':
            return 'monthly'
    return None



class DaftscraperItem(scrapy.Item):
    daftid = scrapy.Field(input_processor = MapCompose(str.strip, extract_number))

    date_scraped = scrapy.Field()

    url = scrapy.Field()

    address = scrapy.Field()

    rent_frequency = scrapy.Field(input_processor = MapCompose(extract_frequency))

    price = scrapy.Field(input_processor = MapCompose(str.strip, extract_number))

    price_currency = scrapy.Field(input_processor = MapCompose(get_currency))
    
    rent_frequency = scrapy.Field(input_processor = MapCompose(extract_frequency))

    property_type = scrapy.Field()

    beds = scrapy.Field(input_processor = MapCompose(extract_number))

    baths = scrapy.Field(input_processor = MapCompose(extract_number))

    description = scrapy.Field(input_processor = MapCompose(description_clean))

    date_listed = scrapy.Field(input_processor = MapCompose(dateparser.parse))
    
    views = scrapy.Field(input_processor = MapCompose(extract_number))
