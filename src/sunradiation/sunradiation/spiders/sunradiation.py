import scrapy

class SunRadiation(scrapy.Spider):
    name = "Sun Radiation"
    allowed_domains = ["eosweb.larc.nasa.gov"]
    url_retscreen_data = "https://eosweb.larc.nasa.gov/cgi-bin/sse/retscreen.cgi?email=rets%40nrcan.gc.ca&step=1&lat=-34.92125&lon=-57.954333299999995&submit=SubmitRE"


    def get_values():
        return response.extract()[0].split[2]

    def parse(self, response):
        poi = SunRadiationItem()
        radiation = response.xpath('/html/body/div[4]/table/tr[15]/td[4]/text()').extract()[]
        wind = response.xpath('/html/body/div[4]/table/tr[15]/td[6]/text()').extract()[]
        earth_temp = response.xpath('/html/body/div[4]/table/tr[15]/td[7]/text()').extract()[]
        elevation = response.xpath('/html/body/div[3]/table/tr[4]/td[3]/text()').extract()[]
        unit = response.xpath('/html/body/div[3]/table/tr[8]/td[2]/text()').extract()[]
        value = response.xpath('/html/body/div[3]/table/tr[8]/td[3]/text()').extract()[]

        poi['latitude'] = lat
        poi['longitude'] = long
        poi['elevation'] = float(elevation)
        poi['avg_solar_radiation'] = float(radiation)
        poi['avg_wind_speed'] = float(wind)
        poi['avg_earth_temperature'] = float(earth_temp)
        poi['frost'] = float(unit)
        poi['frost_unit'] = value
        yield poi
