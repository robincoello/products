import scrapy

class ProductosSpider(scrapy.Spider):
    name = "productos"
    allowed_domains = ["nanotechproject.org"]
    
    
    start_urls = [
        "http://www.nanotechproject.org/cpi/products/"
    ]

    def parse(self, response):
        filename = 'pro.txt'
        scraped = response.xpath("//h5/a").extract()
        print scraped
        print '----------------------------------------------'
        file = open(filename, 'rw+')  
        for sel in response.xpath('//h5'):
			title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract()
			desc = sel.xpath('text()').extract()
			print title, link, desc       
			file.writelines(link)	
			file.writelines('\n')			   	
        file.close()
