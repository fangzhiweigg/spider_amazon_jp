# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item

import scrapy

# class DetailpageItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     ASIN = Field()  # 备份的ASIN。
#     keyword = Field()  # 备份的ASIN。
#     commodity_item = Field()  # 商品名称。
#     brandName = Field()  # #品牌卖家
#     price = Field()  # 价格
#     comments = Field()  # 评论数。
#     star_level = Field()  # 星级
#     ranking = Field()  # 排名
#     DATE = Field()  # ASIN码。
#
#     pass


class DetailpageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ASIN = scrapy.Field() # 备份的ASIN。
    # keyword = scrapy.Field()  # 备份的ASIN。
    commodity_item = scrapy.Field()  # 商品名称。
    brandName = scrapy.Field()# #品牌卖家
    price =scrapy.Field() # 价格
    comments = scrapy.Field()  # 评论数。
    star_level = scrapy.Field()  # 星级
    ranking = scrapy.Field()  # 排名
    login_information = scrapy.Field()  # 登録情報。
    desc_information = scrapy.Field()  # 詳細情報。
    ranking_href = scrapy.Field()  # 日期。

    img = scrapy.Field()  # 日期。

    pass

