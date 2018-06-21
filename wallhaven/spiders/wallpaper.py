# -*- coding: utf-8 -*-
import scrapy
from wallhaven.items import WallhavenItem

class WallpaperSpider(scrapy.Spider):
    name = 'wallpaper'
    allowed_domains = ['wallhaven.cc']
    baseurl='https://alpha.wallhaven.cc/toplist?page='
    page=1
    start_urls=[baseurl+str(page)]

    def parse(self, response):
        id_list=response.xpath('//*[@id="thumbs"]/section/ul/li/figure/@data-wallpaper-id').extract()
        for id in id_list:
            item=WallhavenItem()
            item['image_id']=id
            item['image_url']='https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg'%(id)


            yield item
            if self.page<157:  #翻页值依据网站更新速度自己手动设置
                self.page+=1
                url=self.baseurl+str(self.page)
                yield scrapy.Request(url,callback=self.parse)
