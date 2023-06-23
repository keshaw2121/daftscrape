# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class DescriptionPipeline:

    def process_item(self, item, spider):
        adapter =  ItemAdapter(item)

        if adapter.get('Description'):
            description = adapter['Description']
            adapter['Description'] = description.replace('\n','').replace('\r','').replace('*','')
            return item
        else:
            raise DropItem(f"Missing price in {item}")
