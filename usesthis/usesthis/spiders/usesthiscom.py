from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from usesthis.items import ProfileItem

class UsesthisSpider(BaseSpider):
    name = "usesthis.com"
    allowed_domains = ["usesthis.com"]
    start_urls = [
        "http://usesthis.com/archives",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for url in hxs.select('//ul[@id="interviews"]/li/a/@href').extract():
            yield Request(url=url, callback=self.parse_profile)

    def parse_profile(self, response):
        hxs = HtmlXPathSelector(response)
        item = ProfileItem()
        item['name'] = hxs.select('//h2[@class="person"]/text()').extract()[0]
        item['summary'] = hxs.select('//p[@class="summary"]/text()').extract()[0]
        item['image_url'] = hxs.select('//img[@class="portrait"]/@src').extract()[0]
        item['published'] = hxs.select('//time/@datetime').extract()[0]
        linfo = hxs.select('//article[@class="contents"]/p[2]').extract()
        item["info"] = linfo[0] if linfo else None
        xshardware = hxs.select('//p[./following-sibling::*[@id="and_what_software"] and ./preceding-sibling::*[@id="what_hardware_are_you_using"]]')
        def extract_product(xpath):
            def _extract(xp):
                lxp = xpath.select(xp).extract()
                return lxp[0] if lxp else None
            return {
                "url": _extract("@href"),
                "product": _extract("text()"),
                "ut_id": _extract("@title"),
            }
        item["hardware"] = [extract_product(xp) for xp in xshardware.select("./a")]
        xssoftware = hxs.select('//p[./following-sibling::*[@id="what_would_be_your_dream_setup"] and ./preceding-sibling::*[@id="and_what_software"]]')
        item["software"] = [extract_product(xp) for xp in xssoftware.select("./a")]
        yield item

