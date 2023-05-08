import scrapy


class DollartoeurospiderSpider(scrapy.Spider):
    name = "dollartoeurospider"
    allowed_domains = ["europound.es"]
    start_urls = ["http://www.europound.es/es/inicio-2/?valor=4663"]

    def parse(self, response):
        divisas = response.css("li.list-money")
        for divisa in divisas:
            yield{
                "nombre" : divisa.css("a::text").get(),
                "importe" : divisa.css("p::text").get(),
            }

