# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JoblistingsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    location = scrapy.Field()
    skills = scrapy.Field()
    experience = scrapy.Field()
    salary = scrapy.Field()
    url = scrapy.Field()
    company_website = scrapy.Field()
    #recruiter = scrapy.Field()

