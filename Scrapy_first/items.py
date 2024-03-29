# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TestItem(Item):
    # define the fields for your item here like:
    # name = Field()

    url = Field()
    name = Field()
    price = Field()
    publication = Field()
    author = Field()
    desc = Field()
    belong = Field()
    pass
