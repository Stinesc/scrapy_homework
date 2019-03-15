import scrapy
from ..items import LordandtaylorItem


class JeansSpider(scrapy.Spider):
    name = "jeans"
    start_urls = ['https://www.lordandtaylor.com/Men/Apparel/Jeans/shop/_/N-4ztf06/Ne-6ja3o7?sre=MHP_MODPE2_L1_PROMO_MENS']
    prefix_url = "https://www.lordandtaylor.com"

    def parse(self, response):
        pages_urls = response.xpath('//ol[@class="pa-page-number"]/li/a/@href').extract()

        for url in pages_urls:
            yield scrapy.Request(self.prefix_url+url, callback=self.parse_category)

    def parse_category(self, response):
        urls = response.xpath('//a[@class="mainBlackText"]/@href').extract()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        fields_item = LordandtaylorItem()
        fields_item["title"] = response.xpath("//a[@class='product-overview__brand-link']/text()").extract()
        fields_item["image"] = response.xpath("//meta[@property='og:image']/@content").extract()
        fields_item["size"] = response.xpath("//li/span[@class='']/text()").extract()
        fields_item["price"] = response.xpath("//span[@itemprop='price']/@content").extract()
        fields_item["description"] = response.xpath("//div[@itemprop='description']/text()").extract()
        fields_item["color"] = response.xpath("//dd[@class='product-variant-attribute-label__selected-value']/text()").extract()
        return fields_item
