import scrapy


class DetailsSpider(scrapy.Spider):
    name = 'details'
    allowed_domains = ['eprocure.gov.in']
    start_urls = [
        'https://eprocure.gov.in/cppp/latestactivetendersnew/cpppdata/']

    def parse(self, response):
        details = response.xpath('//tbody/tr/td[5]/a')
        for link in details:
            title = link.xpath('.//text()').get()
            ln = link.xpath('.//@href').get()

            yield response.follow(url=ln, callback=self.get_detail, meta={'name': title})

    def get_detail(self, response):
        name = response.meta['name']
        cap = response.xpath('//div[@class="captcha"]/img/@alt/text()').get()

        yield {
            'Title': name,
            'captcha': cap
        }
