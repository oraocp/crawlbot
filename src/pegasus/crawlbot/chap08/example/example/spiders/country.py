# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ExampleItem


class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/index/', deny='/user/'), follow=True),
        Rule(LinkExtractor(allow=r'/view/', deny='/user/'), callback='parse_item'),
    )

    def parse_item(self, response):
        item = ExampleItem()
        name_css = 'tr#places_country_row td.w2p_fw::text'
        item['name'] = response.css(name_css).extract()
        pop_css = 'tr#places_population_row td.w2p_fw::text'
        item['population'] = response.css(pop_css).extract()
        return item
