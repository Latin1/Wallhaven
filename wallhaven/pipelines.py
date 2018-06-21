# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings #获取项目路径的settings配置项
from scrapy.pipelines.images import ImagesPipeline #管道保存图片的基类
import os
import scrapy

class WallhavenPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
        # return item

    images_store=get_project_settings().get('IMAGES_STORE')
    def get_media_requests(self,item,info):
        image_url=item['image_url']
        yield scrapy.Request(image_url)
    def item_completed(self,results,item,info):
        image_path = [x["path"] for true,x in results if true]
        try:
            os.rename(self.images_store+'/'+image_path[0],self.images_store+'/'+item['image_id']+".jpg")
        except Exception:
            pass
        return item
