# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ProfileItem(Item):
    # define the fields for your item here like:
    # name = Field()
    name = Field()
    summary = Field()
    image_url = Field()
    published = Field()
    info = Field()
    hardware = Field()
    software = Field()
