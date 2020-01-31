# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # country = response.xpath("//td/a//text()").getall()
        # links = response.xpath("//td/a/@href").getall()
        countries = response.xpath("//td/a")
        for count in countries:
            # name = count.xpath(".//text()").get()
            link = count.xpath(".//@href").get()

            # yield {
            #     'title' : name ,
            #     'countries':link
            # } 

            #link is realative url without domain and protocol
            absolute_url = "https://www.worldometers.info{}".format(link)
            yield scrapy.Request(url=absolute_url)