# -*- coding: utf-8 -*-  
  
BOT_NAME = 'dwowan_gif_spider'  
  
SPIDER_MODULES = ['dwowan_gif_spider.spiders']  
NEWSPIDER_MODULE = 'dwowan_gif_spider.spiders'  
  
  
#启动对应的Pipeline，有多个Pipeline时，数字小的先执行  
ITEM_PIPELINES={'dwowan_gif_spider.pipelines.GifPipeline': 1}  