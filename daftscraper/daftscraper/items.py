# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DaftscraperItem:
    DaftID: Optional[str] = field(default=None)
    Url: Optional[str] = field(default=None)
    Address: Optional[str] = field(default=None)
    Price: Optional[str] = field(default=None)
    Property_Type: Optional[str] = field(default=None)
    Beds: Optional[str] = field(default=None)
    Baths: Optional[str] = field(default=None)
    Description: Optional[str] = field(default=None)
    Date_Listed: Optional[str] = field(default=None)
    Views: Optional[str] = field(default=None)
