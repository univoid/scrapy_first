# -*- coding: utf-8 -*-

# Scrapy settings for Scrapy_first project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Scrapy_first'

SPIDER_MODULES = ['Scrapy_first.spiders']
NEWSPIDER_MODULE = 'Scrapy_first.spiders'
ITEM_PIPELINES = ['Scrapy_first.pipelines.TestPipeline']
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Scrapy_first (+http://www.yourdomain.com)'
