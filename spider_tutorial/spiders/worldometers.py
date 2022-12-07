import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):

        for row in response.xpath('//tr'):

            # title = response.xpath('//h1/text()').get()
            countries = row.xpath('./td[2]/a/text()').getall()
            population = row.xpath('./td[3]/text()').getall()

            yield {
                'coutnries': countries,
                'population': population,
            }
