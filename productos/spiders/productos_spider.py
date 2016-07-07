import scrapy

class ProductosSpider(scrapy.Spider):
    name = "productos"
    allowed_domains = ["nanotechproject.org"]
    start_urls = [
        "http://www.nanotechproject.org/cpi/products/"
    ]

    def parse(self, response):
        filename = 'pro.txt'
        scraped = response.xpath("//h5/text()").extract()
        f = open(filename, 'rw+')
        f.seek(0, 2)
        f.writelines(scraped)
        f.writelines('\n')
        f.close()
