import scrapy

class ProductosSpider(scrapy.Spider):
    name = "productos"
    allowed_domains = ["nanotechproject.org"]
    start_urls = [
        "http://www.nanotechproject.org/cpi/products/"
    ]

    def parse(self, response):
        filename = 'productos.txt'
        scraped = response.xpath("//h5").extract()
        print scraped
        print '*************************'
        with open(filename, 'rw+') as f:            
            f.write(scraped)            
            
