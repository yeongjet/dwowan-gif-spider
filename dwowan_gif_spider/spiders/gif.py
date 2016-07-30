#-*- coding: utf-8 -*-  
#coding：UTF-8  
from scrapy.contrib.spiders import CrawlSpider, Rule  
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor  
from dwowan_gif_spider.items import GifItem  
  
  
class GifSpider(CrawlSpider):  
  
    #爬虫名字，唯一，用于区分以后新建的爬虫  
    name = "dwowan_gif_spider"  
  
    #可选，定义爬取区域，超出区域的链接不爬取  
    allowed_domains = ["duowan.com"]  
      
    #定义开始爬取的页面A  
    start_urls=["http://tu.duowan.com/gallery/127033.html"]  
      
    #定义规则，在页面A中爬取符合规则的链接，并调用函数处理  
    rules = [  
        Rule(SgmlLinkExtractor(allow=('/scroll/\d*/\d*.html')),  callback = 'parse_gif', follow=True),  
        Rule(SgmlLinkExtractor(allow=('/scroll/\d*.html')),  callback = 'parse_gif', follow=True),  
        ]  
  
    def parse_gif(self, response):  
        #定义获取数据的结构  
        urlItem = GifItem()  
          
        #注意item是每个页面的数据集合,每个页面有一个item，搜集整理好交给Pipeline处理  
        urlItem['gif_url'] = response.selector.xpath('//*[@id="picture-pageshow"]/div[1]/div[@class="pic-box"]/a/img/@src').extract()  
        yield urlItem 