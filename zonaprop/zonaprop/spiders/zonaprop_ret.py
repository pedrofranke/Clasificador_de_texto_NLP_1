import scrapy



class ZonapropRetSpider(scrapy.Spider):
    name = "zonaprop_ret"
    allowed_domains = ["zonaprop.com.ar"]
    start_urls = ["https://www.zonaprop.com.ar/ph-alquiler-capital-federal.html"]

    custom_settings = {
        'COOKIES_ENABLED': False,  # Deshabilita las cookies
        'DOWNLOAD_DELAY': 2,  # Agrega un retraso entre las descargas
    }

    def start_requests(self):
        custom_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

        for url in self.start_urls:
            yield scrapy.Request(url, headers=custom_headers, callback=self.parse)
    
    def parse(self, response):
        div_selector = response.css('div.sc-1uhtbxc-0.hpNmeK')
        extracted_text = div_selector.css('::text').get()
        print("Texto extraído:", extracted_text)
