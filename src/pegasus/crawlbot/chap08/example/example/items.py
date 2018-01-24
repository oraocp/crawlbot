# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    """
    定义爬虫运行时想要存储的待抓取国家信息
    """
    # define the fields for your item here like:

    # 国家名称
    name = scrapy.Field()
    # 人口数量
    population = scrapy.Field()
