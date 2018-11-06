## 		                                                        批量下载Wallhaven上的高品质壁纸	



![](https://forthebadge.com/images/badges/built-with-love.svg)![](https://forthebadge.com/images/badges/made-with-python.svg)





![](https://i.loli.net/2018/03/08/5aa154476ec86.jpg)



- 图片采集后自动批量重命名，图片名称为图片ID

- 保存位置在`wallhaven/setting.py`中的`IMAGES_STORE`可以自行更改路径

- 网站服务器在境外，爬取速度有可能稍慢，受带宽影响

- 克隆仓库

  ```
  git clone https://github.com/Latin1/wallhaven.git
  ```

- 进入wallhaven/spiders

  ```
  cd wallhaven/spiders
  #运行spider
  scrapy crawl wallpaper
  ```
