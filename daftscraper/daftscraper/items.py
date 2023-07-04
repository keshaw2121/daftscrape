# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DaftscraperItem:
    daftid: Optional[str] = field(default=None)
    url: Optional[str] = field(default=None)
    date: Optional[str] = field(default=None)
    address: Optional[str] = field(default=None)
    price: Optional[str] = field(default=None)
    property_type: Optional[str] = field(default=None)
    beds: Optional[str] = field(default=None)
    baths: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    date_listed: Optional[str] = field(default=None)
    views: Optional[str] = field(default=None)
