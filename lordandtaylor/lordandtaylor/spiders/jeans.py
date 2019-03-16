import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import LordandtaylorItem


class JeansSpider(RedisSpider):
    name = "jeans"
    #start_urls = ['https://www.lordandtaylor.com/Men/Apparel/Jeans/shop/_/N-4ztf06/Ne-6ja3o7?sre=MHP_MODPE2_L1_PROMO_MENS']
    prefix_url = "https://www.lordandtaylor.com"

    #def make_requests_from_url(self, url):


    def parse(self, response):
        pages_urls = response.xpath('//ol[@class="pa-page-number"]/li/a/@href').extract()

        for url in pages_urls:
            yield scrapy.Request(self.prefix_url+url, callback=self.parse_page)

    def parse_page(self, response):
        urls = response.xpath('//a[@class="mainBlackText"]/@href').extract()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        fields_item = LordandtaylorItem()
        fields_item["title"] = response.xpath("//a[@class='product-overview__brand-link']/text()").extract()
        fields_item["image"] = response.xpath("//meta[@property='og:image']/@content").extract()
        fields_item["size"] = self.parse_size(response)
        fields_item["price"] = response.xpath("//span[@itemprop='price']/@content").extract()
        fields_item["description"] = response.xpath("//div[@itemprop='description']/text()").extract_first()
        fields_item["color"] = response.xpath(
            "//dd[@class='product-variant-attribute-label__selected-value']/text()").extract()
        return fields_item

    def parse_size(self, response):
        sizes = response.xpath("//li/span[@class='']/text()").extract()
        if not sizes:
            sizes = response.xpath(
            "//select[@class='drop-down-list__select drop-down-list__select--default']/option[not(@value='')]/text()"
            ).extract().split(" ", 1)[0]
        return sizes
