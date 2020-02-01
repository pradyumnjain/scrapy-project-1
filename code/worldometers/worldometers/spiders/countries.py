# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for count in countries:
            name = count.xpath(".//text()").get()
            link = count.xpath(".//@href").get()
            #link is realative url without domain and protocol
            #absolute url is the inverse of relative url 
            absolute_url = "https://www.worldometers.info{}".format(link)
            #or
            absolute_url = response.urljoin(link)
            
            # yield scrapy.Request(url=absolute_url)
            #or
            # yield response.follow(url=link)
            yield {
                'name':name
            }
            yield response.follow(url=link,callback=self.parse_country,meta={'country_name':name})
    
    def parse_country(self,response):
        # logging.info(response.url) #gives th elof of the response we get back from the response url
        name = response.request.meta['country_name']
        rows = response.xpath("(//div[@class='table-responsive'])[1]//tbody/tr")
        for row in rows:
                year = row.xpath(".//td[1]/text()").get()
                population = row.xpath(".//td[2]/strong/text()").get()

                yield {
                    "name":name,
                    "year": year,
                    "population":population
                }

