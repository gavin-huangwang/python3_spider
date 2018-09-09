# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item

#中华网定义item
class TongyongSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=Field()
    text=Field()
    datetime=Field()
    url=Field()
    website=Field()

#微博item
#用户详情
class Useritem(Item):
    collection = 'users'
    id = Field()
    name = Field()
    avatar = Field()
    cover = Field()
    gender = Field()
    description = Field()
    fans_count = Field()
    follows_count = Field()
    weibos_count = Field()
    verified = Field()
    verified_reason = Field()
    verified_type = Field()
    follows = Field()
    fans = Field()
    crawled_at = Field()

#粉丝和关注
class UserRelationitem(Item):
    collection ='users'
    id = Field()
    follows = Field()
    fans = Field()

#微博
class Weiboitem(Item):
    collection ='weibos'
    id = Field()
    attitudes_count = Field()
    comments_count = Field()
    reposts_count = Field()
    picture = Field()
    pictures = Field()
    source = Field()
    text = Field()
    raw_text = Field()
    thumbnail = Field()
    user = Field()
    created_at = Field()
    crawled_at = Field()

