#-*- coding: utf-8 -*-  
#coding：UTF-8  
  
import scrapy  
  
#自定义要获取的数据Item的结构  
class GifItem(scrapy.Item):  
    #自定义数据item的结构,这里的item只有gif_url一项  
    #要获取更多的数据，可以增加item的项  
    gif_url = scrapy.Field()  
    pass  