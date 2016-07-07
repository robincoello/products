import scrapy

class ProductosSpider(scrapy.Spider):    
    name = "productos"
    allowed_domains = ["nanotechproject.org"]
    
     		
    start_urls = [
        "http://www.nanotechproject.org/cpi/products/",        
    ]
    for x in range(1,76):
		print x
		start_urls.append("http://www.nanotechproject.org/cpi/products/page" + str(x));  
		  

    def parse(self, response):
	sitio = 'http://www.nanotechproject.org'
        filename = 'pro.txt'
        print '----------------------------------------------'
        file = open(filename, 'rw+')  
        file.seek(0,2)   
        for sel in response.xpath('//h5'):
			#title = sel.xpath('a/text()').extract()
			link = sel.xpath('a/@href').extract()
			#desc = sel.xpath('text()').extract()			
			print link  			
			file.writelines(sitio)				
			file.writelines(link)				
			file.writelines('\n')					  
	file.close()
