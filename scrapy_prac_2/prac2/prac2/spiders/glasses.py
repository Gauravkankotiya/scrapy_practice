import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath("//div[@class='product-img-outer']/a[1]")
        names = response.xpath(
            "//div[1]/main/div[3]/div[3]/div[2]/div[2]/div/div[1]/div[4]/div[2]/div/div[1]/div/a[1]")
        prices = response.xpath("//div[@class='p-price']/div[1]/span[1]")

        for product, name, price in zip(products, names, prices):
            pro_link = product.xpath('.//@href').get()
            pro_img = product.xpath('.//img[1]/@src').get()
            pro_name = name.xpath('//text()').get()
            pro_price = price.xpath('.//text()').get()

            yield {
                'Product Link': pro_link,
                'Product Image': pro_img,
                'Product Name': pro_name,
                'Product Price': pro_price
            }

        next_page = response.xpath(
            "//li[6]/a[@class='page-link']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
