import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http//172.18.58.80/creative/']