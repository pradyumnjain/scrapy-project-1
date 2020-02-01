# -*- coding: utf-8 -*-
import scrapy


class GdpratioSpider(scrapy.Spider):
    name = 'gdpratio'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        table =  response.xpath("//table[@class='table table-striped']/tbody/tr")
        for tab in table:
            name = tab.xpath(".//td/a/text()").get()
            gdp = tab.xpath(".//td[2]/text()").get()
            population = tab.xpath(".//tr/td[3]/text()").get()

            yield {
                'name' : name,
                'gdp'  : gdp,
                'population' : population
            }

