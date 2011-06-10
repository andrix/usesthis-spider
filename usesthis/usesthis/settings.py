# Scrapy settings for usesthis project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrapy/usesthis'
BOT_VERSION = '0.1'

SPIDER_MODULES = ['usesthis.spiders']
NEWSPIDER_MODULE = 'usesthis.spiders'
DEFAULT_ITEM_CLASS = 'usesthis.items.ProfileItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

