# -*- coding: utf-8 -*-
import scrapy
from qimo.items import QimoItem

class HouseSpider(scrapy.Spider):
    name = 'house'

    start_urls = ['https://sz.lianjia.com/ershoufang/pg'+str(i)+'/' for i in range(1,101)]
    def parse(self, response):
        li = response.xpath('//ul[@class="sellListContent"]/li')
        for lis in li:
            link = lis.xpath('.//div[@class="title"]/a/@href').extract_first()
            url = response.urljoin(link)
           # print(url)
            yield scrapy.Request(url=url, callback=self.parse_content)

    def parse_content(self, response):
        title = response.xpath('//h1[@class="main"]/text()').extract_first()
        price = response.xpath('.//div[@class="price "]/span/text()').extract_first()+"万"
        unitprice = response.xpath('.//div[@class="unitPrice"]/span/text()').extract_first()+"元/平米"
        maininfo = response.xpath('.//div[@class="mainInfo"]/text()').extract_first()
        subinfo = response.xpath('.//div[@class="subInfo"]/text()').extract_first()
        area = response.xpath('.//div[@class="area"]/div[@class="mainInfo"]/text()').extract_first()
        xiaoqu = response.xpath('.//div[@class="communityName"]/a/text()').extract_first()
        # dizhi1 = response.xpath('.//div[@class="areaName"]/a/text()').extract_first()
        # dizhi2 = response.xpath('.//div[@class="areaName"]/span[@class="info"]/a/text()').extract()
        dizhi = ""
        dizhi2 = dizhi.join(response.xpath('.//div[@class="areaName"]/span[@class="info"]/a/text()').extract())
        address = dizhi2
        brokername = response.xpath('.//div[@class="brokerName"]/a/text()').extract_first()
        phone1 = response.xpath('.//div[@class="phone"]/text()').extract_first()
        phone2 = response.xpath('.//div[@class="phone"]/span[@class="phone-text"]/text()').extract_first()
        phone3 = response.xpath('.//div[@class="phone"]/text()').extract()[1]
        phone = phone1+phone2+phone3
        # print(dizhi1)
        # print(dizhi2)
        # print(title)
        # print(price)
        # print(unitprice)
        # print(maininfo)
        # print(subinfo)
        # print(area)
        # print(xiaoqu)
        # print(address)
        # print(brokername)
        # print(phone)
        # print("-------------------------------")
        item = QimoItem()
        item['title'] = title
        item['price'] = price
        item['unitprice'] = unitprice
        item['maininfo'] = maininfo
        item['subinfo'] = subinfo
        item['area'] = area
        item['xiaoqu'] = xiaoqu
        item['address'] = address
        item['brokername'] = brokername
        item['phone'] = phone
        yield item