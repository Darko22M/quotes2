# -*- coding: utf-8 -*-
import scrapy

#allows items to be loaded
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
	
    #This MUST be named parse
    def parse(self, response):
    	
    	l = ItemLoader(item=QuotesSpiderItem(), response = response)

    	quotes = response.xpath("//div[@class='quote']")
    	for quote in quotes:
    		text = quote.xpath(".//*[@class='text']/text()").extract_first()
    		author = quote.xpath(".//*[@itemprop='author']/text()").extract_first()
    		tags = quote.xpath(".//*[@itemprop='keywords']/@content").extract()
    		
    		l.add_value('text', text)
    		l.add_value('author', author)
    		l.add_value('tags', tags)

    	yield l.load_item()
    	"""
    	next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()

    	absolute_next_page_url = response.urljoin(next_page_url)
    	yield scrapy.Request(absolute_next_page_url)
		"""