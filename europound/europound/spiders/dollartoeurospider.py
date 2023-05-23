import scrapy
from europound.items import DollarItem

class DollartoeurospiderSpider(scrapy.Spider):
    name = "dollartoeurospider"
    allowed_domains = ["europound.es"]
    start_urls = ["http://www.europound.es/es/inicio-2/?valor=4663"]

    # custom_settings = {
    #     "FEEDS" : {
    #         "dollardata.json" : { "format" : "json", "overwrite": False}
    #     }
        
    # }

    def parse(self, response):
        divisas = response.css("li.list-money")
        dollar = DollarItem()
        dollar["nombre"] = divisas[1].css("a::text").get(),
        dollar["importe"] = divisas[1].css("p::text").get(),
        yield dollar
        

