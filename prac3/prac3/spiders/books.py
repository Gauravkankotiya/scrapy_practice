import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
    )

    def parse_item(self, response):
        yield {
            'Book Name': response.xpath('//div/h1/text()').get(),
            'Book Price': response.xpath("//p[@class='price_color']/text()").get(),
        }
