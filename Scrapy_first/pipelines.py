# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo

class TestPipeline(object):
    con = pymongo.Connection("localhost", 27017)
    db = con.spider

    def process_item(self, item, spider):
        if item['url'] == "":
            return item

        dbdata = {"name":"", "url":"", "price":"", "publication":"", "author":"", "desc":"", "belong":""}
        dbdata["name"] = item['name']
        dbdata["url"] = item['url']
        dbdata["price"] = item['price']
        dbdata["publication"] = item['publication']
        dbdata["author"] = item['author']
        dbdata["desc"] = item['desc']
        dbdata["belong"] = item['belong']

        try:
            self.db.booklist.insert(dbdata)
        except:
            print "====================================insert error"

        return item
