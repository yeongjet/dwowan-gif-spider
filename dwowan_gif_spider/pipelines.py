#-*- coding: utf-8 -*-  
#coding：UTF-8  
import urllib  
import urllib2  
import time  
import os    
import shutil  
from scrapy.exceptions import DropItem  
import pymongo  
  
#Pineline用于处理获取到的item数据  
class GifPipeline(object):  
  
    #启动爬虫时执行，新建一个名为gif_download的文件  
    #创建一个名为gif_url的mongo数据库, 并创建一个集合my_collection  
    #创建一个名为gif_url的txt文件  
    def __init__(self):  
        conn = pymongo.MongoClient('localhost', 27017)  
        db = conn['gif_url']  
        self.collection = db['gif_collection']  
  
        self.f = open('url_gif.txt', 'wb')  

        if os.path.exists('gif_download'):    
            shutil.rmtree("gif_download")    
        else:    
            os.mkdir("gif_download")
  
  
    #爬虫启动时调用，处理获取到的item数据,注意item是每一个页面的数据集合  
    def process_item(self, item, spider):  
        #去除没用的数据  
        if item['gif_url']:  
              
            #遍历每个页面item集合里面的所有url  
            #字符串判断，过滤所有.jpg和.png文件，只下载gif文件  
            #将url插入mongo数据库  
            #将url存放进txt，稍后可以用迅雷下载  
            for i in item['gif_url']:  
                if ".gif" in i:  
                    self.f.write(i)  
                    self.f.write('\r\n')  
  
                    gif_url=[{"url":i}]  
                    self.collection.insert(gif_url)  
                  
                    now = time.localtime(time.time())  
                    fname = str(now)  
                    urllib.urlretrieve(i, 'gif_download/%s.gif' %fname)  
        else:  
            raise DropItem(item)  
        return item  
  
  
    #爬虫关闭时调用  
    def close_spider(self, spider):  
        print("Done")  