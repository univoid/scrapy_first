from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from Scrapy_first.items import TestItem

class test(CrawlSpider):
    name = "test"
    allowed_domains = ["yuedu.baidu.com"]
    start_urls = ["http://yuedu.baidu.com/book/list/0?od=0&show=1&pn=0"]
    rules = [Rule(SgmlLinkExtractor(allow=('/ebook/[^/]+fr=booklist')), callback='myparse'),
             Rule(SgmlLinkExtractor(allow=('/book/list/[^/]+pn=[^/]+', )), follow=True)]

    def myparse(self, response):
        x = HtmlXPathSelector(response)
        item = TestItem()

        item['url'] = response.url
        item['name'] = ""
        item['price'] = ""
        item['publication'] = ""
        item['author'] = ""
        item['desc'] = ""
        item['belong'] = ""

        strlist = x.select("//h1/@title").extract()
        if len(strlist) > 0:
            item['name'] = strlist[0]

        strlist = x.select("//div[@class='doc-info-price']//span[@class='txt-now-price-num']/text()").extract()
        if len(strlist) > 0:
            item['price'] = strlist[0]

        strlist = x.select("//ul[@class='doc-info-org']")
        if len(strlist) > 0:
            item['author'] = strlist.select("li[1]/a").text()
            item['publication'] = strlist.select("li[2]/a").text()

        strlist = x.select("//div[@class='des-content']/p/text()").extract()
        if len(strlist) > 0:
            item['desc'] = strlist[0]

        strlist = x.select("//li/a[contains(@data-logsend, 'send')]/text()").extract()

        belong = ""
        index = 0
        for str in strlist:
            index += 1
            if index <= 1:
                continue

            if len(belong) <= 0:
                belong += str
            else:
                belong += "->"+str

        item['belong'] = belong

        self.log(item['url']+"    "+item['name'])
        return item